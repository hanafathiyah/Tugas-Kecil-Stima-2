import numpy as np

def jarak_titik_ke_titik(titik1, titik2):
    return np.sqrt((titik1[0] - titik2[0]) ** 2 + (titik1[1] - titik2[1]) ** 2) 