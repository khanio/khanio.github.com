Title: Linux Containers (lxc) For Developer's Soul
Date: 2013-04-28 23:15
Tags: ubuntu, lxc, libvirt, virtualization
Category: Virtualization
Slug: linux-containers-for-developers-soul
Author: Zakiullah Khan Mohammed
Summary: When working with different technology stacks, it becomes necessary to maintian clean slate environment, and for this Linux Containers comes to rescue. This post walks through the basic steps required to setup an isolated web server container on Ubuntu 12.04 host.

If you have been using Linux Virtual Machines (VM) on a day to day basis to setup various development environments, one limitation you will notice that the more virtual isntances you spawn the performance of host deteriorates, meaning at times when you need more processing power or memory at host level,it isn't available as needed. This is where Linux Contianers (LXC) steps in, they let you harness all the barebone resources and yet maintain process and filesystem isolation.

LXCs are not fit for all situations, but if you are like me whose day to day job is to spawn linux instances and work out different integration scenarios, and only need to isolate processes and filesystem, LXCs tend to do the job. When compared to a VM, LXC is more lightweight, well bootstraped to the host OS and above all easier to maintain and backup. One serious disadvantage of LXC is hardware resource sharing between different contianers, especially hard drive access at same time.

Now lets get started, before we move forward, below detailed steps are for Ubuntu 12.04 as host operationg system, if you are using OSX or Windows operating system, you can still give LXC a shot using Virtualbox or VMWare virtual machine, or using vagrant from command line.

First lets get lxc and libvirt installed, for this run the following at your command prompt.

    >sudo apt-get install lxc libvirt-bin dnsmasq bridge-utils debootstrap

Once installed successfully, rebooting the machine is required as the network bridge (virbr0) setup by libvirt during installation will be active after reboot. Once you are back to your console after reboot, run the following to see the virtual netwrok bridge details, which is setup by libvirt.

    >virsh net-info default

If all looks good, create a sample container with identifier name as *sample_cntr*, this will take few mintues to setup depending your internet connection speed. Just like vagrant, lxc allows you to use pre-defined instance templates, and in our case we are using the *ubuntu* template.

    >sudo lxc-create -t ubuntu -n sample_cntr

Once the container is created, every time you start the container a new IP is assigend to the instance, as we are trying to setup a web server container, it would be advisable to have a static IP address defined for the container. For this we need to edit the container's config file

    >sudo vim /var/lib /lxc/sample_cntr/config

 To allow the container use the libvirt defined default virtual network bridge, edit the following line

    lxc.network.link = lxcbr0

to

    lxc.network.link = virbr0

And to have a static IP address assigned every time its starts, add the following line, note the IP address depends on your preference, run *ifconfig* before to determine virbr0 network bridge details.

    lxc.network.ipv4=192.168.122.100/24

Now we are done with the house keeping stuff, lets start the container in the background

    >sudo lxc-start -n sample_cntr -d

Now lets get to the container command prompt and setup a nginx web server, for this at your command prompt run

    >sudo lxc-console -n sample_cntr

You will be prompted for login credentials, for the *ubuntu* template container the default username/password is ubuntu/ubuntu. Once successfully logged in, run the following to setup simple nginx web server.

    >sudo apt-get install nginx-full
    >sudo service nginx start

Now you can point your browser to the contianer's IP and see the default nginx web page get displayed. To stop the contianer you can do it by running the following at your command prompt.

    >sudo lxc-stop -n sample_cntr

To move forward you can give a try to dotcloud's [docker](http://docker.io "Docker"), which is like vagrant for linux contianers.