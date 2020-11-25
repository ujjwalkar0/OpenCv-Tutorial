import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    a=cv2.waitKey(1)

    if a==27: # & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()