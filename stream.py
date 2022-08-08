from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.streamon()

width = 1000
height = 650

while (True):
    frame_read = tello.get_frame_read()
    frame = frame_read.frame
    img = cv2.resize(frame,(width,height))

    cv2.imshow("Stream",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

