#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import local, env, put, run
import os

env.hosts = ['54.167.171.207', '54.172.80.33']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploys an archive to the servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_filename = os.path.basename(archive_path)
        release_dir = '/data/web_static/releases/' + archive_filename[:-4]
        run('sudo mkdir -p {}'.format(release_dir))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_dir))

        # Remove the uploaded archive
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Move the extracted files to the correct location
        run('sudo mv {}/web_static/* {}'.format(release_dir, release_dir))

        # Remove the web_static symbolic link
        run('sudo rm -rf {}/web_static'.format(release_dir))

        # Delete the current symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_dir))

        print('New version deployed!')
        return True

    except Exception as e:
        print('Deployment failed:', e)
        return False
