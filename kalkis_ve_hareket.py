from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

iha = connect("127.0.0.1:14550", wait_ready=True)

# print(iha.is_armable)
# print(iha.armed)
# iha.mode = VehicleMode("GUIDED")
# iha.armed = True 
# iha.simple_takeoff(10)

def takeoff(irtifa):
    while iha.is_armable is not True:
        print("İHA arm edilebilir durumda değil.")
        time.sleep(1)


    print("İHA arm edilebilir.")

    iha.mode = VehicleMode("GUIDED")

    iha.armed = True

    while iha.armed is not True:
        print("İHA arm ediliyor...")
        time.sleep(0.5)

    print("İHA arm edildi.")

    iha.simple_takeoff(irtifa)
    
    while iha.location.global_relative_frame.alt < irtifa * 0.9:
        print("İha hedefe yükseliyor.")
        time.sleep(1)
    

takeoff(10)

konum = LocationGlobalRelative(-35.36223671, 149.16509335, 20)

iha.simple_goto(konum)

