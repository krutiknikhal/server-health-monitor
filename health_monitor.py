import platform
import shutil

print ("Server Health Monitor")

hostname = platform.node()
operating_system = platform.system()

print("Hostname:", hostname)
print("Operating System:", operating_system)

c_drive = shutil.disk_usage("C:\\")
d_drive = shutil.disk_usage("D:\\")
e_drive = shutil.disk_usage("E:\\")

gb = 1024 ** 3

print("C Drive Total:", round(c_drive.total / gb,2), "GB")
print("C Drive Used:", round(c_drive.used / gb,2), "GB")
print("C Drive Free:", round(c_drive.free / gb,2), "GB")

print("D Drive Total:", round(d_drive.total / gb, 2), "GB")
print("D Drive Used:", round(d_drive.used / gb, 2), "GB")
print("D Drive Free:", round(d_drive.free / gb, 2), "GB")

print("E Drive Total:", round(e_drive.total / gb, 2), "GB")
print("E Drive Used:", round(e_drive.used / gb, 2), "GB")
print("E Drive Free:", round(e_drive.free / gb, 2), "GB")



