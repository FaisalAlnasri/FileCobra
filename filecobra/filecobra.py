import os
from errors import *

def create(url, is_dir = False, overwrite=False, contents = ''):
    """
    adds a new empty file/directory in a specifed path
    ------------------
    url -> path of the file
    is_dir -> True if you want to make a directory, False by default
    overwrite -> True if you want to overwrite existing file.
    contents -> the contents you want the file to have
    """
    if is_dir:
        if not os.path.isdir(url):
            os.mkdir(url)
    else:
        if not os.path.isfile(url) or overwrite:
            f = open(url, 'w')
            f.write(contents)

def delete(url):
    """
    deletes a file/directory in a specifed path
    ------------------
    url -> path of the file
    """
    if os.path.isfile(url):
        os.remove(url)
    elif os.path.isdir(url):
        try:
            os.rmdir(url)
        except OSError:
            raise DirectoryNotEmpty("cant delete directory, must be empty")

def move(url, new_url):
    """
    moves file to a new location
    ------------------
    url -> current path of the file
    new_url -> new path of the file
    """
    if not os.path.isfile(new_url):
        os.rename(url, new_url)

def rename(url, new_name):
    """
    moves file to a new location
    ------------------
    url -> path of the file
    new_name -> the name you want the file to be
    """
    # TODO: optimise the code below
    url_path_names = url.split('\\')
    if len(url_path_names) >= 2:
        name = '\\'.join(url_path_names[:-1]) + '\\' + new_name # replace the orignal file name with the new name
    else:
        name = new_name

    if os.path.isfile(url):
        os.rename(url, name)

def check(url) -> bool:
    """
    return True if a file/directorys exists
    ------------------
    url -> path of the file
    """
    return os.path.isfile(url) or os.path.isdir(url)

if __name__ == "__main__":
    # for testing purposes
    pass
