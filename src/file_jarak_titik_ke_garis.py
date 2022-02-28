import numpy as np

def jarak_titik_ke_garis(titik1, titik2, titik3):
  
    titik_1_as_numpy = np.array(titik1)
    titik_2_as_numpy = np.array(titik2)
    titik_3_as_numpy = np.array(titik3)

    vektor_a = titik_3_as_numpy - titik_1_as_numpy
    vektor_b = titik_2_as_numpy - titik_1_as_numpy
    vektor_c = np.sum(vektor_a * vektor_b) / np.sum(vektor_b * vektor_b) * vektor_b - vektor_a

    return np.sum(vektor_c * vektor_c)