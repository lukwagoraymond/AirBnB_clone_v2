#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the
web_static folder of my AirBnB clone repo
"""

from datetime import datetime
from fabric.api import local, env
from os.path import isdir

env.user = 'ubuntu'
env.hosts = ['54.165.12.83', '54.237.93.128']


def do_pack():
    """Generates archive file from contents of Clone repo"""
    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tqz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)
    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
