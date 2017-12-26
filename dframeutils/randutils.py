import os

__all__ = ["ListFiles"]


def ListFiles(path, extensions=['.csv']):
    """
    lists the files in a given path

    Parameters:
    ___________

    path:
        a path to the directory (str)

    extensions:
        list of file extensions, to be listed (default: csv)

    returns:
    _______

        list

    """
    assert(os.path.exists(path))
    path.rstrip('/')
    for f in os.listdir(path):
        if ''.join(['.', f.split('.')[-1].lower()]) in extensions:
            yield os.path.join(path, f)
