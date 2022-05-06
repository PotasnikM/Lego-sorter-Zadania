"""Twoim zadaniem jest przechwycenie obrazu z kamerki.
Do tego zadania wystarczy biblioteka OpenCV."""

import cv2


""""Miejsce na Twoje rozwiązanie"""


while True:
    """"Miejsce na Twoje rozwiązanie"""

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
