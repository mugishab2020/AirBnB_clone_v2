#!/usr/bin/python3
# inporting the modules nedded
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar zipped archive of the directory web_static."""
    # setting stand_time
    stand_time = datetime.now().strftime("%Y%m%d%H%M%S")
    # The name of the archive
    archive_path = "versions/web_static_{}.tgz".format(stand_time)
    # making dir version if not exist using local
    local("mkdir -p versions")
    # archiving the forder using tar comand
    archived = local("tar -cvzf {} web_static".format(archive_path))
    if archived.return_code != 0:
        return None
    else:
        return archive_path
