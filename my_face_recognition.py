import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\Face_Recognition\\haarcascade_frontalface_default.xml') # We load the cascade for the face.
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Face_Recognition\\haarcascade_eye.xml') # We load the cascade for the eyes.

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
    return frame

video_capture = cv2.VideoCapture(0)  #0 for internal webcam
while True:
    _, frame = video_capture.read()  #gets us the last frame of the webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()
