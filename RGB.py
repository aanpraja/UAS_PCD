import cv2

image = cv2.imread("Rose.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,biner = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

cv2.imshow("Citra Asli", image)
cv2.imshow("Citra RGB", gray)
cv2.imshow("Citra biner", biner)
cv2.waitKey(0)
cv2.destroyAllWindows()