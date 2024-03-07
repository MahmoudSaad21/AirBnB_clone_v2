#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import local, env, put, run
from os import path

env.hosts = ['54.167.171.207', '54.172.80.33']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        dest = "/tmp/{}".format(file_name)

        put(archive_path, dest)
        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("tar -xzf {} -C /data/web_static/releases/{}/".format(dest, folder_name))
        run("rm {}".format(dest))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(folder_name, folder_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(folder_name))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
