import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from fer import FER
import os
import time
import tensorflow as tf
cascFile = "haarcascade_frontalface_default.xml"
cascPath = os.path.join("haarcascades", cascFile)
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log', level=log.INFO)


""" index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1
    print(index)
print(arr) """

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)
thickness = 2
lineType = 2

video_capture = cv2.VideoCapture('tests/mix.mp4')
#video_capture = cv2.VideoCapture(0)
anterior = 0
lastTime = time.time() - 5
label = "No emotion"


def analyzeEmotion(test_image):
    emo_detector = FER(mtcnn=True)
    emotion = emo_detector.top_emotion(test_image)
    return emotion


while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if time.time()-lastTime > 5:
            lastTime = time.time()
            test_image = crop_img = frame[y:y+h, x:x+w]
            emotion = analyzeEmotion(test_image)
            if emotion[1] is None:
                label = "No emotion"
            else:
                label = "{} at {}%".format(emotion[0], emotion[1]*100)

        cv2.putText(frame,
                    label,
                    (x, y),
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
