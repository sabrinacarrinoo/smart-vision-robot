import cv2
import numpy as np

def detect_obstacles(frame):
    """
    Converte immagine in edges per rilevare ostacoli
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    return edges


def get_obstacle_density(edges):
    """
    Calcola quanto spazio è occupato da ostacoli
    """
    return np.mean(edges)
