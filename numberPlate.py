import cv2
cap=cv2.VideoCapture(0)
framewidth=640
frameheight=480
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,200)
count=0
numberPlate=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea=500
color=(255,0,0)
while True:
    sucess,img=cap.read()
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    plate=numberPlate.detectMultiScale(grayImg,1.1,10)
    for (x,y,w,h) in plate:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"Number Plate",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgRec=img[y:y+h,x:x+w]
            cv2.imshow("Number plate",imgRec)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite("resources/scans/num"+str(count)+".jpg",imgRec)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Image Saved",(100,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
