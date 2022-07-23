#
# Python:   3.10.5
#
# Author:   Jack Johnson
#
# Purpose:  The Tech Academy - Python Course, Creating a program that will
#           check a specific folder on the hard drive, verify whether those
#           files end with a “.txt” file extension and, if they do, print
#           those qualifying file names and their corresponding modified
#           time-stamps to the console. 



import os
import time

path = "/Users/johnjohnson/Document/GitHub/Python_Projects/Script_Assign_214/Python_Script_Assign"

fileList = os.listdir(path)

file = os.path.join(path,"")

mtime = os.path.getmtime(file)
local_time = time.ctime(mtime)


def find_txt():
    for file in fileList:
        if file.endswith(".txt"):
            print("File: ", file, "last modified: ", local_time)
        

if __name__ == "__main__":
    find_txt()
