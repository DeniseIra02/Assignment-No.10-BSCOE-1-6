import cv2
import pyzbar.pyzbar as pyzbar
import datetime


#def function for output
def barc_read(frame):
    #date and time
    date_time = datetime.datetime.now()
    #set module pyzbar and funtion decode
    d_barcodes = pyzbar.decode(frame)

def forcam():

    web_camera = cv2.VideoCapture(0)
    web_camera.set(3,640)
    web_camera.set(4,480)
 
    while True:
        other, frame = web_camera.read()
        barc_read(frame)
        #to show the title of the window
        cv2.imshow('Scanner', frame)
        #loading time
        key = cv2.waitKey(1)
        if key == 27:
            break
  
    web_camera.release()
    cv2.destroyAllWindows()

forcam()