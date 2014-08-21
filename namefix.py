#!/usr/bin/python

import sys
import os
import os.path
import gc
#import shutil

y=len(sys.argv)
if (y!=3):
	print "Usage : ./namefix.py <directory path> <Manga Name>"
	sys.exit()

directory=sys.argv[1]
manga=sys.argv[2]
#print directory
os.chdir(directory)
count=1
searchchar='.'
for filename in sorted(os.listdir(directory)):	
	index=filename.find(searchchar)
	newname=filename[index:]
	newname=manga+"_"+str(count)+newname
	count=count+1

	if os.path.exists(newname):
		print "Cowardly refusing to write over existing file!\n"
		sys.exit()

	os.rename(filename,newname)	
gc.collect()		
print "Successfully renamed " + str(count-1) + " files\n"
sys.exit()	
#print 'Renamed:',directory
