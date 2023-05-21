from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil

iha = connect("127.0.0.1:14550", wait_ready=True)

def takeoff(irtifa):
    while iha.is_armable is not True:
        print("IHA arm edilebilir durumda degil.")
        time.sleep(1)


    print("IHA arm edilebilir.")

    iha.mode = VehicleMode("GUIDED")

    iha.armed = True

    while iha.armed is not True:
        print("IHA arm ediliyor...")
        time.sleep(0.5)

    print("IHA arm edildi.")

    iha.simple_takeoff(irtifa)
    
    while iha.location.global_relative_frame.alt < irtifa * 0.9:
        print("Iha hedefe yükseliyor.")
        time.sleep(1)

def gorev_ekle():
    global komut
    komut = iha.commands

    komut.clear()
    time.sleep(1)

    # TAKEOFF
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10))

    # WAYPOINT
    #WP1
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36318851,149.16530765, 20))
    #WP2
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36306134,149.16534294, 30))
    #WP3
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0,  -35.36293531,149.16531408, 30))
    #WP4
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36289050,149.16519092, 30))
    #WP5
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0,  -35.36275671,149.16505814, 30))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0,  -35.36260512,149.16516322 , 30))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36274486,149.16529055, 30))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0,  -35.36288258,149.16523718, 30))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36303211,149.16508348   , 30))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_SPLINE_WAYPOINT, 0, 0, 0, 0, 0, 0,   -35.36317663,149.16511453, 30))
    # RTL
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    
    # DOĞRULAMA
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    komut.upload()
    print("Komutlar yUkleniyor...")


takeoff(10)

gorev_ekle()

komut.next = 0

iha.mode = VehicleMode("AUTO")

while True:
    next_waypoint = komut.next

    print(f"Siradaki komut {next_waypoint}")
    time.sleep(1)

    if next_waypoint is 5:
        print("Gorev bitti.")
        break


print("Donguden cikildi.")