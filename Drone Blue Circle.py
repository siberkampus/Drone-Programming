import cv2
from cv2 import circle
import numpy as np  
import time
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
def goto_position_target_local_ned(north, east, down):
    """
    Send SET_POSITION_TARGET_LOCAL_NED command to request the drone fly to a specified
    location in the North, East, Down frame.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        north, east, down,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    # send command to drone
    vehicle.send_mavlink(msg)


vehicle = connect('127.0.0.1:14550',wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


arm_and_takeoff(10)

print("Set default/target airspeed to 3")
vehicle.airspeed = 3
cap = cv2.VideoCapture(0)
#0 İD'li kamera "cap" olarak adlandırılır 
while(True): 
    ret,frame = cap.read() 
    #Kameradan okunan görüntüler "frame" değişkenine atılır 
    frame = cv2.flip(frame, 1)
    #Alınan görüntü Y eksenine göre yansıtılır. (Sağ el kaldırıldığında görüntüde de sağ el kalkar)
    frame_lab = cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
    #Alınan görüntü BGRA2BGR formarmatına dönüştürülür
    frame_lab = cv2.medianBlur(frame_lab, 3)
    #Görüntü üzerinde BLURLAMA yapılır
    frame_lab =  cv2.cvtColor(frame_lab, cv2.COLOR_BGR2Lab)
    #Görüntü BGR2Lab formatına dönüştürülür
    lower_red = np.array([20, 115, 70])
    #Algılamak istediğimiz en düşük KIRMIZI renk kodu belirlenir
    upper_red = np.array([255, 145, 100])
    #Algılamak istediğimiz en yüksek KIRMIZI renk kodu belirlenir
    masked_frame = cv2.inRange(frame_lab,lower_red, upper_red)
    #İstediğimiz Kırmızı renk skalasındaki alan "masked_frame" değişkenine atılır.
    masked_frame = cv2.GaussianBlur(masked_frame, (5, 5), 2, 2)
    #İstediğimiz Kırmızı renk skalasındaki görüntü Blurlanır
    circles = cv2.HoughCircles(masked_frame, cv2.HOUGH_GRADIENT, 1, masked_frame.shape[0] / 8, param1=100, param2=18, minRadius=15, maxRadius=60)
    #Hough Circle fonksiyonu görüntü üzerine hayali çemberler çizerek gerçek daire tespiti yapmamızı sağlar
    #Tespit ettiği daireleri "circles" içine atar
    #Parametreler : İşlenecek görüntü , Çember tespiti için kullanılacak method,Ölçek değeri ,Çemberler arası mesafe,ilk eşik değeri,ikinci eşik değeri,
    #Görüntü üzerindeki çemberlerin minimum çapı,görüntü üzerindeki çemberlerin maksimum çapı
    cv2.circle(frame,(320,240),3,(255,255,255),-1)
    
    #Eğer circles boş değilse
    if circles is not None: 
        #Veri tipi dönüşümü yapılır
        circles = np.uint16(np.around(circles))
        #max = circle[0]
    
        biggest_circle=circles[0][0]
        
        for i in circles[0,:]:
            if(i[2]>biggest_circle[2]):
                biggest_circle=i

        
            
        center = (biggest_circle[0], biggest_circle[1])
        # circle merkez koordinatları
        cv2.circle(frame, center, 1, (0, 255, 0), 3)
        # Merkeze küçük circle çizilir
        radius = biggest_circle[2] #Yarıcap
        cv2.circle(frame, center, radius, (0, 255, 0), 3)
        #Yarıcaplı bir circle çizilir
        cv2.putText(frame, "Merkez", (center), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
        #CENTER[0] =320 CENTER[1]=240
            
        if (center[0]<290):{
            goto_position_target_local_ned(0,-1,0),
            #time.sleep(1)
        }
        elif(center[0]>350):{
            goto_position_target_local_ned(0,1,0),
            #time.sleep(1)
        }
        else:{
            print("Dur")
        }
        if(center[1]<210):{
            goto_position_target_local_ned(1,0,0),
            #time.sleep(1)
        }
        elif(center[1]>260):{
            goto_position_target_local_ned(-1,0,0),
            #time.sleep(1)
        }
        else:{
            print("Dur")
        }
            
            #Merkez noktasına "Merkez" çıktısı yazılır
    cv2.imshow("Mask",masked_frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()