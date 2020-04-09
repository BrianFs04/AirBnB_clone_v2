#!/usr/bin/python3
"""Script that generates a .tgz archive
from the contents of the web_static"""
from fabric.api import local
import datetime
import os


def do_pack():
    currtime = datetime.datetime.now()
    now = currtime.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(now)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
