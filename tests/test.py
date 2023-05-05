#samo za video gdje se nešto miče
import cv2 as cv

video = cv.VideoCapture(0)
subtractor = cv.createBackgroundSubtractorMOG2(500, 200)

while True:
    ret, frame = video.read()
    
    #ako imamo frame u videu, stavit ćemo na njega masku
    #ako nemamo, video ne postoji
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        #ako je pritisnut 'X', program će prestati raditi
        if cv.waitKey(5) == ord('X'):
            break

    else:
        video = cv.VideoCapture(0)

#zatvaramo streamove
cv.destroyAllWindows()
video.release()