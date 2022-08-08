import pygame
from djitellopy import Tello
import threading

pygame.joystick.init()
pygame.init()
joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

tello = Tello()
tello.connect()

while True:    
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                # print(event)
                # print(event.button)
                if event.button ==1:
                    print('takeoff ')
                    tello.takeoff()

                elif event.button == 5:
                    print(f'Battery Charge {tello.get_battery()}%')        
                    # print('battery')
                elif event.button == 4:
                    print(f"Temperature : {tello.get_temperature()}")
                    
                elif event.button == 7:
                    print(f"Height: {tello.get_height()} cm")
                    
                elif event.button == 0:
                    print("Landing..") 
                    tello.land()  
                elif event.button == 3:
                    print("taking_picture")
                elif event.button == 2:
                    print("recording_video")        

                elif event.button == 6:
                    tello.end()
                #     increase_speed
            if event.type == pygame.JOYAXISMOTION:

                # print(event)
                # print(event.axis)
                # print(event.value)

                    
                if event.value < -0.3 and event.axis == 1:
                    print('forward')
                    tello.send_rc_control(0,50,0,0)
                    
           
                elif event.value > 0.3 and event.axis == 1:
                    print('Back') 
                    tello.send_rc_control(0,-50,0,0)

                elif event.value > 0.3 and event.axis == 0:
                    print('right')
                    tello.send_rc_control(50,0,0,0)
                    
                elif event.value < -0.3 and event.axis ==0:
                    print('left')
                    tello.send_rc_control(-50,0,0,0)

                    

        
