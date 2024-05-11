import cv2
import face_recognition

cap = cv2.VideoCapture(0)

color = (0, 0, 255)

while True:
    _, frame = cap.read()
    
    faceLocs = face_recognition.face_locations(frame)

    for index, faceLoc in enumerate(faceLocs):
        topLeftY, bottomRightX, bottomRightY, topLeftX = faceLoc

        #detectedFaces = frame[topLeftY : bottomRightY, topLeftX : bottomRightX]

        cv2.rectangle(frame, (topLeftX, topLeftY), (bottomRightX, bottomRightY), color, 3)
    
    cv2.imshow("cam", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()