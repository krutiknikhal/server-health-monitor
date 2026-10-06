import platform

print ("Server Health Monitor")

hostname = platform.node()
operating_system = platform.system()

print("Hostname:", hostname)
print("Operating System:", operating_system)