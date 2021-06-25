import os
import errors

def create(*urls, is_dir=False, overwrite=False):
    """
    adds a new empty file/directory in a specifed path
    ------------------
    urls -> path of file/s
    is_dir -> True if you want to make a directory, False by default
    overwrite -> True if you want to overwrite existing file.
    """
    if is_dir:
        for url in urls:
            if not os.path.isdir(url):
                os.mkdir(url)
    else:
        for url in urls:
            if not os.path.isfile(url) or overwrite:
                open(url, 'w')

def delete(*urls):
    """
    deletes a file/directory in a path
    ------------------
    urls -> path of file/s
    """
    for url in urls:
        if os.path.isfile(url):
            os.remove(url)
        elif os.path.isdir(url):
            try:
                os.rmdir(url)
            except OSError:
                raise errors.DirectoryNotEmpty("cant delete directory, must be empty")
            
def delete_extension(url, extension):
    """
    deletes multiple files with same the extension in a path
    ------------------
    url -> path of the file's parent
    extension -> extension of file (Ex: '.py')
    """
    for f in os.listdir(url):
        if '.' in f:
            if f[f.index('.'):] == extension:
                os.remove(url + "\\" + f)

# TODO: fix move function
def move(*urls, new_url):
    """
    moves file to a new location
    ------------------
    urls -> current path of file/s
    new_url -> new path of file/s (leave empty if you want it to be your current)
    """
    for url in urls:
        if not os.path.isfile(new_url):
            if new_url == '':
                os.rename(url, new_url + url)
            else: 
                os.rename(url, new_url + "\\" + url)

def move_extension(url, new_url, extension):
    """
    moves multiple files with the same extension to a new location
    ------------------
    url -> current path of the file
    new_url -> new path of the file
    extension -> extension of file (Ex: '.py')
    """
    for f in os.listdir(url):
        if '.' in f: # checks if its a file and not a directory
            if f[f.index('.'):] == extension:
                if not os.path.isfile(new_url):
                    if new_url == '':
                        os.rename(url + "\\" + f, f)
                    else:
                        os.rename(url + "\\" + f, new_url + "\\" + f)
    

# TODO: fix rename function
def rename(**kwargs):
    """
    renames multiple files
    ------------------
    kwargs -> change the names like this:
    rename("test.txt" = "new.txt", "main.c" = "main.py")
    """
    for url, new_name in kwargs.items():
        url_names = url.split('\\')
        if len(url_names) >= 2:
            name = '\\'.join(url_names[:-1]) + '\\' + new_name # replace the orignal file name with the new name
        else:
            name = new_name

        if os.path.isfile(url):
            os.rename(url, name)

def check(url) -> bool:
    """
    return True if a file/directory exists
    ------------------
    url -> path of the file
    """
    return os.path.isfile(url) or os.path.isdir(url)

def listfiles(url='', list_files=True, list_dirs=True) -> list:
    """
    lists files/directories in a path
    ------------------
    url -> path of the file
    list_files -> True if you want to include files
    list_dirs -> True if you want to include directories
    """
    list_ = []
    if not list_files and not list_dirs: # if an idiot made them both false
        return list_
        
    if url == '':
        list_ = os.listdir()
    else:
        list_ = os.listdir(url)

    if not list_files:
        list_ = [l for l in list_ if not '.' in l]
    elif not list_dirs:
        list_ = [l for l in list_ if '.' in l]
    
    return list_


if __name__ == "__main__":
    # for testing purposes
    pass