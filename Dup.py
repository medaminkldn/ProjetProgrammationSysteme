import os
fd = os.open("Files/test.txt", os.O_WRONLY)
print("Original file descriptor:", fd)
dup_fd = os.dup(fd)
print("Duplicated file descriptor:", dup_fd)
pid = os.getpid()
os.system("ls -l /proc/%s/fd" %pid)
os.close(fd)
os.close(dup_fd)
print("File descriptor duplicated successfully")
