import platform, psutil, shutil, time, cpuinfo, os



total, used, free = shutil.disk_usage("/")

# print("Disk Used: %d GiB" % (used // (2**30)))


def systemInfo():
    return str(platform.system()) + "; " + str(cpuinfo.get_cpu_info()['brand_raw']) + "; " + str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "; " + str(total // (2 ** 30))
def upadteInfo():
    return str(psutil.virtual_memory().percent) + "; " + str(psutil.cpu_percent()) + "; " + "{:.2f}".format(psutil.cpu_freq().current)

# while True:
#     print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#     print("System: " + platform.system())
#     print(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
#     print("RAM: " + str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB")
#     print("Disk size: %d GiB" % (total // (2 ** 30)))
#
#     print("\n")
#
#     print("Mermory used: " + str(psutil.virtual_memory().percent) + "%")
#     print("CPU usage: " + str(psutil.cpu_percent()) + "%")
#     print("CPU speed: " + str("{:.2f}".format(psutil.cpu_freq().current)) + " Mhz")
#     time.sleep(2)