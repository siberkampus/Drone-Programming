from  dronekit import connect, VehicleMode,LocationGlobalRelative
import time
drone = connect('127.0.0.1:14550',wait_ready=True)
def takeoff(irtifa):
    while drone.is_armable is not True:
        print("Drone arm edilemiyor")
        time.sleep(1)
    drone.mode=VehicleMode("GUIDED")
    time.sleep(1)
    drone.armed=True
    while drone.armed is not True:
        print("Drone arm ediliyor")
        time.sleep(0.5)
    print("Drone Arm Edildi")
    drone.simple_takeoff(irtifa)
#Gerekli kütüphaneler yüklenir
    while drone.location.global_relative_frame.alt < irtifa*0.9:
        print("Drone Yükseliyor")
        time.sleep(0.5)
    


takeoff(4)
konum = LocationGlobalRelative(-80.1111111, 100.22222222, 20)
drone.simple_goto(konum)