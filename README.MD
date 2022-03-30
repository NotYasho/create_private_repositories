yes I am dumb, I didn't know it was possible with the python library `PyGithub`. I realised that after I pushed it and I'm kind of lazy you know

# Installation:
 
 - Run the setup.bat file on Windows
 - (Optional):
   - Set an environment variable for Github-Username and Github-Password
 - Or Modify the username and password variables in the 'push-pr.py'

# What does the 'setup.bat' file do?:

 - Installs all the required modules
 - Moves the push-pr.bat file to the UserProfile
 - Moves the push-pr.py file to the UserProfile

# How to use it?

 - `cd` to The Directory where the folder is located (`cd path/to/folder`)
 - Type `push-pr {Repo-Name}` for Command Prompt
   If that doesn't work:
   - Set an environment variable named 'push-pr' and set the path to `%USERPROFILE%\push-pr.bat`
 - Or you can Run 'push-pr.py' file and follow the on-screen instructions
