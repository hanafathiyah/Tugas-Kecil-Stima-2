from jarak_titik_ke_garis import jarak_titik_ke_garis
from area import membuat_area
import numpy as np

def convex_hull_2(titik1, titik2, area, area_titik):

    # mengecek apakah salah satu dari ketiga elemen tersebut kosong atau tidak
    if (area == [] or titik1 is None or titik2 is None):
        return []

    convex_hull_baru = []

    # menghitung jarak setiap titik dari garis dan mencari titik dengan jarak terjauh
    jarak_terjauh = -1
    titik_terjauh = None
    idx_titik_terjauh = -1
    i = 0

    for titik in area:
        jarak_titik_i_ke_garis = jarak_titik_ke_garis(titik1, titik2, titik)
        if (jarak_titik_i_ke_garis > jarak_terjauh):
            jarak_terjauh = jarak_titik_i_ke_garis
            titik_terjauh = titik
            idx_titik_terjauh = i

        i += 1
    
    convex_hull_baru = convex_hull_baru + [titik_terjauh]

    # menghapus titik terjauh yang sudah terdata
    np.delete(area, idx_titik_terjauh)

    # membuat area
    titik1atas, titik1bawah = membuat_area(titik1, titik_terjauh, area)
    titik2atas, titik2bawah = membuat_area(titik2, titik_terjauh, area)

    if area_titik == "atas":
        convex_hull_baru = convex_hull_baru + convex_hull_2(titik1, titik_terjauh, titik1atas, "atas")
        convex_hull_baru = convex_hull_baru + convex_hull_2(titik_terjauh, titik2, titik2atas, "atas")
    else:
        convex_hull_baru = convex_hull_baru + convex_hull_2(titik1, titik_terjauh, titik1bawah, "bawah")
        convex_hull_baru = convex_hull_baru + convex_hull_2(titik_terjauh, titik2, titik2bawah, "bawah")
