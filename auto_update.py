import os

import win32file
import win32event
import win32con

import glob, os

from solid import *

#http://solidpython.readthedocs.io/en/latest/

import os, solid

os.chdir("./scad.py")
path_to_watch = os.path.abspath (".")

file_times = {}
for file in glob.glob("*.py"):
    file_times[file] = os.stat(file).st_mtime

change_handle = win32file.FindFirstChangeNotification (path_to_watch,0,win32con.FILE_NOTIFY_CHANGE_LAST_WRITE)

try:
    while 1:
        result = win32event.WaitForSingleObject (change_handle, 500)
        if result == win32con.WAIT_OBJECT_0 :
            for file in glob.glob("*.py"):
                statbuf = os.stat(file)
                if (statbuf.st_mtime - file_times[file]) > 0.1 :#100 ms debounce
                    file_times[file] = statbuf.st_mtime
                    print file+": has new save time:",statbuf.st_mtime 
                    cmd = 'python '+'"'+file+'"'
                    print("  => "+os.getcwd()+">"+cmd )
                    os.system(cmd)
            win32file.FindNextChangeNotification (change_handle)
finally:
    win32file.FindCloseChangeNotification (change_handle)

