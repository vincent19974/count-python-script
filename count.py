#!/usr/bin/bash

import os, sys, re
print(sys.version)

path = os.path.dirname(os.path.abspath(__file__))
filepath = path

if os.path.exists(filepath):
    allfiles = "\n".join(os.listdir(filepath))
    file_counting1 = len(re.findall(".fail.txt",allfiles,re.M)) #specific file that you want to count in a specific directory
    print("Total .fail.txt files found:", file_counting1) #print the total files
    file_counting2 = len(re.findall(".config.txt",allfiles,re.M)) #specific file that you want to count in a specific directory
    print("Total .config.txt files found:", file_counting1) #print the total files
