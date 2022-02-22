import os, signal 
pid = os.fork() 
if pid : 
    print("In parent process :") 
    os.kill(pid, signal.SIGSTOP) 
    print("Signal sent, child stopped.") 
    info = os.waitpid(pid, os.WSTOPPED) 
    stopSignal = os.WSTOPSIG(info[1]) 
    print("Child stopped due to signal no:", stopSignal) 
    print("Signal name:", signal.Signals(stopSignal).name) 
    os.kill(pid, signal.SIGCONT)  
    print("Signal sent, child continued.")
      
else : 
    print("In child process :")
    print("Process ID:", os.getpid()) 
    print("Exiting") 