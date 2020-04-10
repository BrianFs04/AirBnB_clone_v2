#!/usr/bin/python3
"""Script that generates a .tgz archive
from the contents of the web_static"""
from fabric.api import *

env.hosts = ['34.74.149.164', '3.93.169.162']
env.user = "ubuntu"


def do_clean(number=0):
    '''Deletes out-of-date archives'''

    number = int(number)

    if number == 1 or number == 0:
        local('cd versions; ls | head -n -1 | xargs rm -rf')
        run('cd /data/web_static/releases; ls | head -n -1 | xargs rm -rf')
    else:
        local('cd versions; ls | head -n -{} | xargs rm -rf'.format(number))
        run('cd /data/web_static/releases; ls | head -n -{} | xargs rm -rf'.
            format(number))
