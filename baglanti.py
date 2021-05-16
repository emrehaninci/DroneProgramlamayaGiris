from dronekit import connect

drone = connect('127.0.0.1:14550', wait_ready=True)

print(f'Drone Arm Durumu: {drone.armed}')

# print(f'Global Frame{drone.location.global_frame}')
# print(f'Global Relative Frame{drone.location.global_relative_frame}')

print(f'İrtifa: {drone.location.global_relative_frame.alt}')