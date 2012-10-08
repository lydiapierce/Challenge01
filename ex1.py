
"""1. Create 26 directories in the current directory, one for each letter of the alphabet:
    ./a/
    ./b/
    ./c/
    etc.

2. Loop through all the files in the original_files directory, and organize each of those files into the directory that their name starts with.

### Example:
    The file named 'artichoke.txt' would go into the directory './a/',
    'bartholomew.txt' would go into './b/'.

Here is a very rough outline of the task components:
* Figure out how to determine a listing of files in a directory (and what format that list is in)
* Figure out how to move a file from one directory to another
* Iterate through your listing of files and determine what the appropriate target directory is"""

import os
import shutil

if not os.path.exists('./newdirs'):
	root_path = './newdirs'
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

	for folder in alpha:
		os.mkdir(os.path.join(root_path,folder))


filenames = os.listdir("./original_files")

for filename in filenames:
	first_char = filename[0]
	target = os.path.join("./newdirs", first_char)
	src_path = os.path.join("./original_files", filename)
	shutil.move(src_path, target)
	# shutil.move( os.path.join("./original_files", filename) ,                 )
	
	# if first_char == "a":
	# 	target = "./newdirs/a"
	# elif first_char == "b":
	# 	target = "./newdirs/b"
# # os.chdir('/Users/student/Desktop/Challenge01/newdirs')

# file_names = os.listdir("")

# if dir_names[0][0]
# shutil.move('/Users/student/Desktop/Challenge01/original_files', '/Users/student/Desktop/Challenge01/newdirs/a')
