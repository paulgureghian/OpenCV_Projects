""" Created in April 2019 by Paul A. Gureghian. """

""" Face detection in images using OpenCV and Python. """ 

### Import OpenCV
import cv2

### Load the cascade
face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml') 
print(face_cascade, '\n')

### Read the input image
img = cv2.imread('/test.jpg')   
print("Color_Image:", img, '\n')

### Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
print("Gray_Image:", gray, '\n')

### Detect faces 
faces = face_cascade.detectMultiScale(gray, 1.1, 4) 

### Draw a rectangle around the faces 
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x ,y), (x+w, y+h), (255, 0, 0), 2)
    
### Display the output
cv2.imshow('image', img)
cv2.waitKey() 
    