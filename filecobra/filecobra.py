import os
from errors import *

def create(url: string, is_dir: bool=False):
    """
    adds a new empty file/directory in a specifed path
    ------------------
        create(url, is_dir=False)
    ------------------
    url: string -> path of the file
    is_dir: bool -> True if you want to make a directory, False by default
    """
    if is_dir:
        if not os.path.isdir(url):
            os.mkdir(url)
    else:
        if not os.path.isfile(url):
            open(url, 'w')

def delete(url: string):
    """
    deletes a file/directory in a specifed path
    ------------------
        delete(url)
    ------------------
    url: string -> path of the file
    """
    if os.path.isfile(url):
        os.remove(url)
    elif os.path.isdir(url):
        try:
            os.rmdir(url)
        except OSError:
            raise DirectoryNotEmpty("cant delete directory")

def move(url: string, new_url: string):
    """
    moves file to a new location
    ------------------
        move(old_path, new_path, filename)
    ------------------
    url: string -> current path of the file
    new_url: string -> new path of the file
    """
    if not os.path.isfile(new_url):
        os.rename(url, new_url)

def rename(url: string, new_name: string):
    """
    moves file to a new location
    ------------------
        move(old_path, new_path, filename)
    ------------------
    url: string -> path of the file
    new_name: string -> the name you want the file to be
    """
    url_path_names = url.split('\\')
    if len(url_path_names) >= 2:
        name = '\\'.join(url_path_names[:-1]) + '\\' + new_name # replace the orignal file name with the new name
    else:
        name = new_name

    if os.path.isfile(url):
        os.rename(url, name)

def check(url: string) -> bool:
    """
    return True if a file/directorys exists
    ------------------
        check(url)
    ------------------
    url: string -> path of the file
    """
    return os.path.isfile(url) or os.path.isdir(url)

if __name__ == "__main__":
    delete('test')