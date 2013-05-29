# Eric Jackson - 2013
import os, fnmatch, sys, fileinput, shutil, stat

# Handle incorrect parameters
def param_error():
	sys.stdout.write("Must specify \"1\" or \"2\" for comment style.\r\n")
	sys.stdout.write("\"1\":\tReplace /* ... */ with \t// ...\r\n")
	sys.stdout.write("\"2\":\tReplace // ...    with \t/* ... */\r\n")
	sys.stdout.write("Ex.:\tcommenter.py 1 *.c\r\n")
	sys.exit(-1)
	
# Yield all files in directory and subdirectories
def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename

# Check for proper user input (need program name [0], comment replace style [1], and file types to parse [2])
if len(sys.argv) < 3:
	param_error()

# Get comment replace style from user
comment_style = sys.argv[1]
sys.stdout.write("Comment style: " + str(comment_style) + "\r\n")

# Only 1 or 2 accepted
if comment_style != "1" and comment_style != "2":
	param_error()
	
# Get file type(s) to parse from user
file_types = sys.argv[2:]
sys.stdout.write("File types to parse: " + str(file_types) + "\r\n")

# Call find_files and process each file type starting from root directory
for ftype in file_types:
	for filename in find_files(".\\", ftype):
		sys.stdout.write(filename + "\r\n")
		
		count1 = 0
		count2 = 0
		for line in fileinput.input(filename, inplace = 1, backup = ".orig"):
			# Replace /* ... */ with // ...
			if comment_style == "1":
				if "/*" in line and "/**" not in line:
					count1 += 1
					
					line = line.replace("/*", "//").rstrip("\r\n")
					line = line.replace("*/", "").rstrip("\r\n")
					
					l = []
					l.append(line)
					l.append("\n")

					s = ''.join(l)
					
					sys.stdout.write(s)
				else:
					sys.stdout.write(line)
			
			# Replace // ... with /* ... */
			elif comment_style == "2":
				if "//" in line:
					count2 += 1

					line = line.replace("//", "/*").rstrip("\r\n")
					line = line.rstrip()
					
					l = []
					l.append(line)
					l.append(" */")
					l.append("\n")

					s = ''.join(l)
					
					sys.stdout.write(s)
				else:
					sys.stdout.write(line)
		
		sys.stdout.write("Got " + str(count1) + " /*'s\r\n")	
		sys.stdout.write("Got " + str(count2) + " //'s\r\n")
