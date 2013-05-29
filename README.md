##Commenter

Python (3.3) script to change all comments in source code files from `/* ... */ to // ...` or vice versa. Drop it in a root directory and it'll work on the current directory as well as all sub-directories.

Backup files are automatically created (with the extension ".orig") in the same folder as the original. If you want to rename these originals later, you can open up command prompt in Windows and do `"ren *.orig *."`.

For now, this only handles the comment styles mentioned above, so any comments in source code using hash-marks ("`#`") and other comment styles won't be affected. Perhaps I'll make this a bit more robust in the future, but this was all I needed at the time :)

###Usage
Examples, typed in the command prompt (shift + right click, "Open command window here") from where the *commenter.py* program resides:

1. `commenter.py 1 *.c *.java`

	This will change comments in all C and Java files from `/* ... */` to `// ...`


2. `commenter.py 2 *.c`

	This will change comments in all C files from `// ...` to `/* ... */`

All files in the current directory **and all sub-directories** will be parsed!

####Note
This was my first Python script, written in 3.3. If there are mistakes or inconsistencies, please let me know.