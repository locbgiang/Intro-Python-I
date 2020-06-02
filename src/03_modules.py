"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('Name of the program:', sys.argv[0])

# Print out the OS platform you're using:
# YOUR CODE HERE
print('Using window', sys.getwindowsversion()[0], 'and platform', sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(f'Using python version {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Process ID is', os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('Current working directory', os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Machine's login name is", os.getlogin())