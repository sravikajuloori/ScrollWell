import cv2


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    cv2.imshow("Video Frame",frame)
    #to close the camera
    key_pressed = cv2.waitKey(1) & 0xFF #(32bit )bitwise anding with 32
    
    if key_pressed==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()