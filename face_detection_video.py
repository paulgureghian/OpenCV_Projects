""" Created in April 2019 by Paul A. Gureghian. """

""" Face detection in videos using OpenCV and Python. """

### Import OpenCV
import cv2

### Load the cascade
face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')

### To capture video from the webcam
cap = cv2.VideoCapture(0)

### To use an mp4 file as input
cap = cv2.VideoCapture('/filename.mp4') 

### Loop through the video frames
while True:
    
    _, img = cap.read() # Read the frame
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Detect the faces
    
    for (x ,y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) # Draw a rectangle around the faces 
        
    ### Display the faces 
    cv2.imshow('image', img)

    ### Stop if escape key is pressed
    k =  cv2.waitKey(30) & 0xff    
    if k == 27:
        break
    
### Release the video capture object
cap.release()         