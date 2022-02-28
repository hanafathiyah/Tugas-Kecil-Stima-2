import numpy as np
from file_membuat_area import membuat_area
from file_jarak_titik_ke_garis import jarak_titik_ke_garis

def fungsi_convex_hull_atas(titik1, titik2, atas_garis):

    # mengecek apakah salah satu dari ketiga elemen tersebut kosong atau tidak
    if (atas_garis == [] or titik1 is None or titik2 is None):
        return atas_garis

    convex_hull_atas = []

    # menghitung jarak setiap titik dari garis dan mencari titik dengan jarak terjauh
    jarak_terjauh = -1
    titik_terjauh = None

    indeks_titik = 0
    indeks_titik_terjauh = -1

    for titik in atas_garis:
        jarak_titik_i_ke_garis = jarak_titik_ke_garis(titik1, titik2, titik)
        if (jarak_titik_i_ke_garis > jarak_terjauh):
            jarak_terjauh = jarak_titik_i_ke_garis
            titik_terjauh = titik
            indeks_titik_terjauh = indeks_titik
        indeks_titik += 1

    convex_hull_atas = convex_hull_atas + [titik_terjauh]

    # menghapus titik terjauh yang sudah terdata
    np.delete(atas_garis, indeks_titik_terjauh)

    # membuat area
    titik1atas, titik1bawah = membuat_area(titik1, titik_terjauh, atas_garis)
    titik2atas, titik2bawah = membuat_area(titik_terjauh, titik2, atas_garis)

    convex_hull_atas = convex_hull_atas + fungsi_convex_hull_atas(titik1, titik_terjauh, titik1atas)
    convex_hull_atas = convex_hull_atas + fungsi_convex_hull_atas(titik_terjauh, titik2, titik2atas)

    return convex_hull_atas