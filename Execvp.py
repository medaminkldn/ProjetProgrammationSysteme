import os
cmd = ["ls", "-l", "-n"]
os.execvp("ls", cmd)