# Wykrywanie butelek na obrazie

## Opis
Projekt skupia się na wykrywaniu butelek na obrazie przy użyciu klasyfikatora kaskadowego.

## Struktura projektu
- `app.py` - skrypt jest prostym narzędziem do wykrywania butelek na obrazie.
- `classifier.py` - skrypt wczytuje obraz i klasyfikator kaskadowy, a następnie wykrywa butelki na obrazie i zaznacza je prostokątami.
- `positives.txt` - każdy wiersz zawiera ścieżkę do obrazu oraz informacje o lokalizacji obiektu (x, y, szerokość, wysokość).
- `negatives.txt` - każdy wiersz powinien zawierać tylko ścieżkę do obrazu.

## Proces treningu
### Stworzenie wektorów
opencv_createsamples -info positives.txt -num <LICZBA_POZYTYWNYCH_OBRAZÓW> -w <SZEROKOŚĆ> -h <WYSOKOŚĆ> -vec positives.vec

### Trening klasyfikatora
opencv_traincascade -data classifier/ -vec positives.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos <LICZBA_POZYTYWNYCH_OBRAZÓW> -numNeg <LICZBA_NEGATYWNYCH_OBRAZÓW> -w <SZEROKOŚĆ> -h <WYSOKOŚĆ> -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024
