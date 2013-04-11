import os
import pwd

from fabric.api import *

def compile():
	local('recess --compress theme/static/less/bootstrap.less > theme/static/css/bootstrap.min.css && make html');

def publish():
	local('recess --compress theme/static/less/bootstrap.less > theme/static/css/bootstrap.min.css && make html && cp -rf output/* ../ && cd .. && git add . && git commit -m "Updated" && git push -u origin master && cd src');
