#!/usr/bin/python3
"""Script that generates a .tgz archive
from the contents of the web_static"""
from fabric.api import local, env, run, put
import datetime
import os

env.hosts = ['34.74.149.164', '3.93.169.162']


def deploy():
    """ Full deployment """
    path = do_pack()

    if not os.path.exists(path):
        return False

    dep = do_deploy(path)
    return dep


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


def do_deploy(archive_path):

    if not os.path.exists(archive_path):
        return False

    pfname = archive_path.split("/")
    fname = pfname[1]
    folder_name = fname.split(".")
    descom_path = "/data/web_static/releases/{}/".format(folder_name[0])
    link_path = "/data/web_static/current"
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(descom_path))
        run("tar -xzf /tmp/{} -C {}".format(fname, descom_path))
        run("rm /tmp/{}".format(fname))
        run("mv {}web_static/* {}".format(descom_path, descom_path))
        run("rm -rf {}web_static/".format(descom_path))
        run("rm -rf {}".format(link_path))
        run("ln -s {} {}".format(descom_path, link_path))
        return True
    except:
        return False
