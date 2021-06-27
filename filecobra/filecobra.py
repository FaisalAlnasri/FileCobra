import os
import errors
import re

def create(*urls, is_dir=False, overwrite=False, contents=''):
    """
    adds a new empty file/directory in a specifed path
    ------------------
    urls -> path of file(s)
    is_dir -> True if you want to make a directory, False by default
    overwrite -> True if you want to overwrite existing file.
    contents -> the contents you want to store in the new file(s)
    """
    if is_dir:
        for url in urls:
            if not os.path.isdir(url):
                os.mkdir(url)
    else:
        for url in urls:
            if not os.path.isfile(url) or overwrite:
                f = open(url, 'w')
                f.write(contents)

def delete(*urls):
    """
    deletes a file/directory in a path
    ------------------
    urls -> path of file(s)
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
                os.remove(url + "/" + f)

def move(*urls, new_url):
    """
    moves file to a new location
    ------------------
    urls -> current path of file(s)
    new_url -> new path of file(s) (leave empty if you want it to be your current)
    """
    for url in urls:
        pattern = re.compile(r'[a-zA-Z\.]+$')
        match = pattern.findall(url)[0]
        if not os.path.isfile(new_url):
            if new_url == '':
                os.rename(url, match)
            else: 
                if '/' in new_url:
                    os.rename(url, new_url + match)
                else:
                    os.rename(url, new_url + "/" + url)

def move_extension(url, new_url, extension):
    """
    moves multiple files with the same extension to a new location
    ------------------
    url -> current path of the file's parent
    new_url -> new path of the file's parent
    extension -> extension of file (Ex: '.py')
    """
    for f in os.listdir(url):
        if '.' in f: # checks if its a file and not a directory
            if f[f.index('.'):] == extension:
                if not os.path.isfile(new_url):
                    if new_url == '':
                        os.rename(url + "/" + f, f)
                    else:
                        os.rename(url + "/" + f, new_url + "/" + f)
    

def rename(url, new_name):
    """
    renames multiple files
    ------------------
    url -> current path of file
    new_name -> new name of file
    """
    url_names = url.split('/')
    if len(url_names) >= 2:
        name = '/'.join(url_names[:-1]) + '/' + new_name # replace the orignal file name with the new name
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

def read(*urls):
    """
    reads multiple/single file(s) and returns a list or string
    ------------------
    urls -> current path of file(s)
    """
    if len(urls) == 1:
        f = open(urls[0], 'r')
        return f.read()
    else:
        res = []
        for url in urls:
            f = open(url, 'r')
            res.append(f.read())
        return res

def write(url, contents, append_mode=True):
    """
    writes to a file
    ------------------
    url -> path of the file
    append_mode -> True if you want to add text, false if you want overwrite the file
    """
    if append_mode:
        f = open(url, 'a')
        f.write(contents)
    else:
        f = open(url, 'w')
        f.write(contents)


if __name__ == "__main__":
    # for testing purposes
    contents = read("test.txt", "te.txt")
    print(contents)
