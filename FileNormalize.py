#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os


def displayUsage():
    print "*************************************************************************"
    print """
    Usage: python FileNormalize.py [-r] [-mFileExternal] TargetDirectory
           r    Recursively walk to sub-directories
           m    File filter mode pattern, such as -mTxt  -mtxt -mTXT
    """
    print "*************************************************************************"
    pass


def normalizeFileName(fileName):
    # TODO: Normalizing file name
    print(fileName.decode("gb2312"))
    pass


def listAllFiles(root=None, methods=None, mode=False, filterStr=None, level=0):
    targetDirectory = os.getcwd() if root is None else root
    if not os.path.isdir(targetDirectory):
        if level == 0:
            print("The target directory does not exists")
        return
    try:
        for f in os.listdir(targetDirectory):
            fPath = os.path.join(targetDirectory, f)
            if os.path.isfile(fPath) and (filterStr is None or f.endswith(filterStr)):
                if methods is None:
                    print(f.decode("gb2312"))
                else:
                    methods(f)
            elif mode and os.path.isdir(fPath):
                listAllFiles(root=fPath, methods=methods, mode=mode, filterStr=filterStr, level=level + 1)
    except WindowsError as winError:
        print(str(winError))
    pass

if __name__ == "__main__":
    """This module should be used to normalize the file name under the given directory """
    if len(sys.argv) < 2:
        displayUsage()
        sys.exit(0)
    # Get the recursive mode, file filters and absolute path of targeting directory
    workingMode = False
    fileFilter = None
    dirPath = None
    for pStr in sys.argv:
        if pStr == "-r":
            workingMode = True
            continue
        if pStr.startswith("-m"):
            fileFilter = pStr[2:].lower()
            continue
        if not pStr.endswith(".py"):
            dirPath = pStr
            dirPath.replace("\\", "/")
            if not dirPath.endswith("/"):
                dirPath += "/"
            continue
    print("Normalizing the name of %sfiles in the target directory %s." %
          (" " if fileFilter is None else fileFilter + " ", "recursively" if workingMode else ""))
    # Normalizing the files' names in the target directory
    listAllFiles(root=dirPath, methods=normalizeFileName, mode=workingMode, filterStr=fileFilter)
    print("Done.")
