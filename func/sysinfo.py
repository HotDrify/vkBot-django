import psutil

cup_per = psutil.cpu_percent(interval=0.5)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage("/")
log_str = "Django Bot"
log_str += "\n| CPU | RAM | DISK |\n"
log_str += "| %dcore | %.2fG | %.2f |\n" % (
    psutil.cpu_count(logical=False),
    memory_info.total / 1024 / 1024 / 1024,
    disk_info.total / 1024 / 1024 / 1024,
)
log_str += "| %s%%  |   %s%%  |   %s%%  |\n" % (
    cup_per,
    memory_info.percent,
    disk_info.percent,
)


def sysinfo():
    return f"{log_str}"
