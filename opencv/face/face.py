import cv2


face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt2.xml')

img = cv2.imread('./images/faces (2).jpg')
img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
faces = face_cascade.detectMultiScale(gray, 1.03, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('TRY 05', img)
cv2.waitKey()