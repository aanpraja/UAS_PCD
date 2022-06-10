import cv2

img = cv2.imread("Rose.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Citra Asli", img)
cv2.imshow("Gambar Hasil Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()