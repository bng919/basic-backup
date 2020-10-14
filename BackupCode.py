# Ben's Backup
# Written by Ben Graham (b.graham@queensu.ca)
# Version 1.0 (written 200810) (comments updated for clairty 201013)
# Makes backup of Desktop and Documents to local removable disk M:
# Must contain folder M:/Backups
# Backups places in folder titled YYMMDD
# Can only execute once per day due to naming covention of folders

userName = 'benng' # Set to computer username

import os
import subprocess
import sys
from datetime import datetime

folderName = datetime.today().strftime('%Y%m%d') # Get date
folderName = folderName[2:] # Remove starting chars (will be '20' for the rest of this century, not a good long term solution but shouldn't be alive to encournter this issue)
newFolderPath = "M:/Backups/" + folderName # New backup folder path

# Make new backup folder
try:
	os.mkdir(newFolderPath)
except OSError:
	print("Err 00: mkdir failure")
	sys.exit("Error making folder. Is the drive connected at M:? Have you already backed up today?")
else:
	print("mkdir success")

# Make new Desktop folder
try:
	os.mkdir(newFolderPath + "/Desktop")
except OSError:
	print("Err 01: mkdir failure")
else:
	print("mkdir success")

# Make new Documents folder
try:
	os.mkdir(newFolderPath + "/Documents")
except OSError:
	print("Err 02: mkdir failure")
else:
	print("mkdir success")

# Set up source and destination folders for copy
sourceFolder1 = r"c:\Users\{}\Desktop".format(userName)
sourceFolder2 = r"c:\Users\{}\Documents".format(userName)
destinationFolder1 = r"M:\Backups\{}\Desktop".format(folderName)
destinationFolder2 = r"M:\Backups\{}\Documents".format(folderName)

#Run xcopy command
subprocess.call(['xcopy', sourceFolder1, destinationFolder1, '/e'])
subprocess.call(['xcopy', sourceFolder2, destinationFolder2, '/e'])
