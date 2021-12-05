import subprocess
import sys
ip = sys.argv[1]
print(ip)
pingCmd = "ping -c 1 " + ip
subprocess.Popen(pingCmd, shell=True)

# Normal operation
# python ./command_injection.py "127.0.0.1"
# Command injection 
# python ./command_injection.py "127.0.0.1 & dir"

# Defense 
# 1) Input validation
# 2) Use a library instead of directly making system calls e.g tcpping
