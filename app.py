import cv2
import numpy as np

def detect_bottles(image_path):
    # Wczytanie obrazu
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Zastosowanie adaptacyjnej progowej binarnizacji
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # Znalezienie konturów
    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Rysowanie prostokątów wokół wykrytych butelek
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Możesz dostosować ten próg w zależności od wielkości butelek
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Wyświetlenie wynikowego obrazu
    cv2.imshow("Detected Bottles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ścieżka do obrazu
image_path = "reg.jpg"
detect_bottles(image_path)





"""
import cv2
import numpy as np

def detect_bottles(image_path):
    # Wczytanie obrazu
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Filtracja obrazu i detekcja krawędzi
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    # Znalezienie konturów na obrazie
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtracja konturów na podstawie ich wielkości (założenie, że butelki mają podobny rozmiar)
    bottle_contours = [c for c in contours if cv2.contourArea(c) > 500]  # wartość 500 można dostosować

    # Rysowanie prostokątów otaczających butelki na oryginalnym obrazie
    for contour in bottle_contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Wyświetlenie wynikowego obrazu
    cv2.imshow("Bottles Detected", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_bottles('reg.jpg')
"""