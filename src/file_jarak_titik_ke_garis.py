import numpy as np

def jarak_titik_ke_garis(titik1, titik2, titik3):
  
    # dimisalkan suatu garis l terbentuk dari titik1 dan titik2
    # fungsi akan me-return jarak titik3 ke garis l tersebut

    # Ax + By + C = 0
    # (y - y1) = m(x - x1)
    # (y - y1)/(y2 - y1) = (x - x1)/(x2 - x1)
    titik_1_as_numpy = np.array(titik1)
    titik_2_as_numpy = np.array(titik2)
    titik_3_as_numpy = np.array(titik3)

    vektor_a = titik_3_as_numpy - titik_1_as_numpy
    vektor_b = titik_2_as_numpy - titik_1_as_numpy
    vektor_c = np.sum(vektor_a * vektor_b) / np.sum(vektor_b * vektor_b) * vektor_b - vektor_a
    # rumus | Ax + By + C | / akar(A^2 + B^2)

    return np.sum(vektor_c * vektor_c)