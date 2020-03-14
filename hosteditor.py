#!/usr/bin/env python
# coding: utf-8

import os ,sys
import shutil
import datetime

def read_file(path):
    dataFile = open(path , 'r')
    dataFileList = dataFile.readlines()
    dataFile.close()
    return dataFileList

PathDataFile = 'C:\\MyScript\\HostFileEditor\\dataFile\\data_file.txt'  # Your NEW complete Host File
PathHostFile = 'C:\\WINDOWS\\system32\\drivers\\etc\\hosts' # Original Host file details
backUpFile = 'C:\\MyScript\\HostFileEditor\\dataFile\\backup\\hosts'
logFile = 'C:\\MyScript\\HostFileEditor\\log.txt'

if __name__=='__main__':
    l_add=''
    l_remove=[]
    reFormating=[]
    logfile= open(logFile , 'a+')
    if os.path.exists(PathHostFile) and os.path.isfile(PathHostFile):
        if os.path.getsize(PathHostFile) < 1708:
            dataFile = read_file(PathDataFile)
            WinHostFile = read_file(PathHostFile)
            for i in dataFile:
                if i not in  WinHostFile:
                    l_add=l_add+i
                else:
                    pass
            for i in WinHostFile:
                if i.strip('#').strip() in [ i.strip() for i in dataFile ] and i not in ['\n' , '#\n']:
                    l_remove.append(i)
            # rewrite file
            reopenHost = open(PathHostFile , 'r+')
            HostFileR=reopenHost.readlines()
            reFormating = [ str(i) for i in HostFileR if i not in l_remove ]
            reFormating.append(l_add)
            ll= ''.join(str(i) for i in reFormating)
            reopenHost.truncate()
            reopenHost.seek(0)
            reopenHost.write(ll)
            reopenHost.close()
            logfile.write("Patch Done ->"+str(datetime.datetime.now()))
            logfile.close()
            sys.exit()
    elif ~os.path.isfile(PathHostFile):
        shutil.copyfile(backUpFile, PathHostFile)
        logfile.write("New Patched Created ->"+str(datetime.datetime.now()))
        logfile.close()
        sys.exit()
    elif os.path.getsize(PathHostFile)==0:
        shutil.copyfile(backUpFile, PathHostFile)
        logfile.write("New Patched Replaced ->"+str(datetime.datetime.now()))
        logfile.close()
        sys.exit()
    else:
        logfile.close()
        sys.exit()     
