import cv2
import pyzbar.pyzbar as pyzbar
import datetime
import numpy as np

#def function for output
def barc_read(frame):
    #date and time
    date_time = datetime.datetime.now()
    #set module pyzbar and funtion decode
    d_barcodes = pyzbar.decode(frame)

    #for loop for webcam scanning
    for barc in d_barcodes:
        #dcode the data
        qR_code = barc.data.decode('utf-8')
        print(qR_code + date_time.strftime("%c"))
        #Add bounding box
        d_pts = np.array([barc.polygon], np.int32)
        d_pts = d_pts.reshape((-1,1,2))
        #polyline function to create the bounding box
        cv2.polylines(frame, [d_pts], True, (255,0,255), 5)
        d_pts2 = barc.rect
        #Add text for the title of the scanner box
        cv2.putText(frame, "CONTACT TRACING", (d_pts2[0], d_pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)

        #for saving the scanned data from qrcode in a text file
        #set mode to 'a' for multiple data scanned
        with open("Result.txt", mode = 'a') as datatxt:
            datatxt.write("Scanned QR Code:\n")
            datatxt.write(qR_code)
            datatxt.write("\n")
            datatxt.write("\n")
            datatxt.write("\n")
            datatxt.write(date_time.strftime("%c"))
            datatxt.write("\n")
            datatxt.write("\n")
            datatxt.write("\n")
            datatxt.close
            
    return barc_read
         
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