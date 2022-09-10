import psutil
import datetime
import subprocess
import os
import time

p = psutil.Process(os.getpid())
cup_per = psutil.cpu_percent(interval=0.5)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage("/")
proc = subprocess.check_output(["ps -eo stime,time,user,args"], shell=True).decode("utf-8")
uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))

log_str = "\n| CPU | RAM | DISK |\n"
log_str+= "| %dcore | %.2fG | %.2f |\n" % (psutil.cpu_count(logical=False), memory_info.total/1024/1024/1024, disk_info.total/1024/1024/1024)
log_str+= "| %s%%  |   %s%%  |   %s%%  |\n" % (cup_per, memory_info.percent, disk_info.percent)
log_str+= "<====PROC====>\n"
log_str+= proc + "\n"
log_str+= "<====UPTIME====>\n"
log_str+= uptime
def sys():
	return f"{log_str}"
