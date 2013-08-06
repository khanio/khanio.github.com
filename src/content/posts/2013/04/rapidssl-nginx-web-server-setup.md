Title: RapidSSL + Nginx Web Server Setup
Date: 2013-04-20 17:17
Tags: nginx, rapidssl, https, ssl
Category: Servers
Slug: rapidssl-nginx-web-server-setup
Author: Zakiullah Khan Mohammed
Summary: This post highlights the steps need to be taken to enable SSL support in Nginx.

Recently I had to setup a Nginx web server with SSL enabled by default. The underlying operating system of the machine was Ubuntu 12.04 (server edition) and the following steps were taken:

First generate a new SSL key on the web server, which we will use later to upload on RapidSSL website to generate the required SSL certificate. Make sure you have openssl installed on your Ubuntu server machine and issue the following at the command prompt, considerations made here are, the domain for which we would be setting up SSL here is www.example.com, Country been US, state been California, Location been San Francisco, Organization name been ACME Corp. and fully qualified domain name been www.example.com, you will nee to replace these values with the required ones.

	>openssl req -new -newkey rsa:2048 -nodes -out www_example_com.csr -keyout www_example_com.key -subj "/C=US/ST=CA/L=San Francisco/O=ACME Corp./CN=www.example.com"

Next head to RapidSSL website and opt to purcahse single domain SSL certificate, you will be required to upload the www_example_com.csr file at the first step, and after successful checkout, you will receive an email from RapidSSL witht he reqired certificates text embedded within the email body. Copy the received text into a file called www_example_com.pem.

Once this is done now issue the following at the command prompt:

	>sudo cp www_example_com.pem /etc/ssl/cert/www_example_com.pem
	>sudo cp www_example_com.key /etc/ssl/key/www_example_com.key

Now we will need to configure Nginx to use by default SSL and divert http traffic on port 80 to 443 (default SSL port). issue th following at the command prompt and replace the contents of _default_ Nginx config with below one.

	>sudo nano /etc/nginx/sites-available/default

Once file opened, delete all content and add the below configuration:

	server {
		listen 80;
		listen 443 default ssl;

		server_name www.example.com;

		root /usr/share/nginx.html;
		index index.html index.htm;

		if ($scheme = http) {
			rewrite ^ https://$server_name$request_uri permanent;
		}

		ssl_certificate /etc/ssl/certs/www_example_com.pem;
		ssl_certificate_key /etc/ssl/www_example_com.key;

		ssl_session_timeout 5m;

		ssl_protocols SSLv3 TLSv1;
		ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv3:+EXP;
		ssl_prefer_server_ciphers on;

		access_log /var/log/nginx/nginx.www_example_com.access.log;
		error_log /var/log/nginx/nginx.www_example_com.error.log;

		location / {
			try_files $uri $uri/ /index.html =404;
		}
	}

Once done save it and restart nginx.

	>sudo service nginx restart

If all goes well you should now be able to use access the web server using https. Also if the web server is an AWS EC2 instance make sure to enable https port (443) on outbound in the required security group.

