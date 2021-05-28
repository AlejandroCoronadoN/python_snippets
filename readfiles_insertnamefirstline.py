import os 
from os import walk

def line_prepender(filename, line):
    """
    Inserts a string (line)  at the begining of a file
    
    Parameters
    ----------
    filename (String): Name of the file
    line (String): String that we want to insert at the begining of the line.
    Returns
    -------
    None.

    """
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        
def insert_line(comment_subfix = "//", mypath = os.getcwd()):
    """
    Read all the files insert mypath and then insert a line at the begining of
    the file. This function is used to mark the files with the name of the file

    Parameters
    ----------
    comment_subfix (String): Subfix that marks a comment in a particular langauge
    Ex: # in python, // in javaScript. optional
    mypath (String): Path of the folder. 
    Returns
    -------
    None.

    """
    _, _, filenames = next(walk(mypath))
    for file in filenames:
        line = file + " " + file 
        path_components = os.getcwd().split("\\")
        line =  comment_subfix + "-------------- " + path_components[-3] + "\\" + path_components[-2] + "\\" + path_components[-1] + " => " + file + " --------------"
        print(line)
        #line_prepender(file, line)
