import cv2

# Wczytaj klasyfikator
bottle_cascade = cv2.CascadeClassifier('classifier/cascade.xml')

# Wczytaj obraz
image = cv2.imread('test_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Wykryj butelki
bottles = bottle_cascade.detectMultiScale(gray, 1.1, 5)

# Narysuj prostokąty wokół butelek
for (x, y, w, h) in bottles:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detected Bottles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
