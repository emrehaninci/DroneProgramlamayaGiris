from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil

iha = connect("127.0.0.1:14550", wait_ready=True)

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

def gorev_ekle():
    global komut
    komut = iha.commands

    komut.clear()
    time.sleep(1)

    # TAKEOFF
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10))

    # WAYPOINT
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36265286, 149.16514170, 20))
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, -35.36318559, 149.16607666, 30))

    # RTL
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    
    # DOĞRULAMA
    komut.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    komut.upload()
    print("Komutlar yükleniyor...")


takeoff(10)

gorev_ekle()

komut.next = 0

iha.mode = VehicleMode("AUTO")

while True:
    next_waypoint = komut.next

    print(f"Sıradaki komut {next_waypoint}")
    time.sleep(1)

    if next_waypoint is 4:
        print("Görev bitti.")
        break


print("Döngüden çıkıldı.")

