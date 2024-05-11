import cv2
import face_recognition

image = cv2.imread("images\cumberbatch.jpg")
image = cv2.resize(image, (450, 450), interpolation= cv2.INTER_AREA)

faceLocs = face_recognition.face_locations(image)
color = (0, 0, 255)

for index, faceloc in enumerate(faceLocs):
    topLeftY, bottomRightX, bottomRightY, topLeftX = faceloc

    detectedFaces = image[topLeftY : bottomRightY, topLeftX : bottomRightX]

    cv2.rectangle(image, (topLeftX, topLeftY), (bottomRightX, bottomRightY), color, 3)

cv2.imshow("cumber", image)
cv2.waitKey(0)
cv2.destroyAllWindows()