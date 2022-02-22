import os  
pid = os.fork() 
if pid : 
    status = os.wait() 
    print("In parent process :") 
    print("Terminated child's process id:", status[0]) 
    print("Signal number that killed the child process:", status[1]) 
  
else : 
    print("In Child process :") 
    print("Process ID:", os.getpid())
    print("Exiting") 