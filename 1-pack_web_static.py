#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    now = datetime.now()
    tgz_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(tgz_file))

    if result.failed:
        return None
    return tgz_file
