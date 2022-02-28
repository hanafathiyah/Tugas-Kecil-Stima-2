import numpy as np
from file_membuat_area import membuat_area
from file_membuat_tipe_numpy import membuat_tipe_numpy
from file_convex_hull_atas import fungsi_convex_hull_atas
from file_convex_hull_bawah import fungsi_convex_hull_bawah
from file_titik_menjadi_indeks import titik_menjadi_indeks

def myConvexHull(array_titik):
    if len(array_titik) <= 2:
        return array_titik

  # membuat array kosong untuk convex hull (menyimpan dalam bentuk titik)
    hasil_convex_hull = []

    urutan_x = sorted(array_titik, key=lambda x: x[0])
    titik1 = urutan_x[0] # Titik minimum
    titik2 = urutan_x[-1] # Titik maksimum

    hasil_convex_hull = hasil_convex_hull + [titik1, titik2]

  # menghapus dari list setelah dimasukkan ke dalam proses convex hull
    urutan_x.pop(0)
    urutan_x.pop(-1)

  #  dnc pertama, membagi 2 area menjadi atas_garis dan bawah_garis
    atas_garis, bawah_garis = membuat_area(titik1, titik2, urutan_x)

  # membagi dua hasil convex_hull, yaitu bagian atas dan bagian bawah
    hasil_convex_hull_atas = []
    hasil_convex_hull_bawah = []
    hasil_convex_hull_atas = hasil_convex_hull + fungsi_convex_hull_atas(titik1, titik2, atas_garis)
    hasil_convex_hull_bawah = hasil_convex_hull + fungsi_convex_hull_bawah(titik1, titik2, bawah_garis)

    hasil_convex_hull_atas = sorted(hasil_convex_hull_atas, key=lambda x: (x[0], -x[1]))
    hasil_convex_hull_bawah = sorted(hasil_convex_hull_bawah, key=lambda x: (x[0], x[1]))

    hasil_convex_hull_atas_as_numpy = membuat_tipe_numpy(hasil_convex_hull_atas)
    hasil_convex_hull_bawah_as_numpy = membuat_tipe_numpy(hasil_convex_hull_bawah)

    return_value_atas = []
    return_value_bawah = []

    for i in range(len(hasil_convex_hull_atas_as_numpy) - 1):
        return_value_atas = return_value_atas + [[titik_menjadi_indeks(hasil_convex_hull_atas_as_numpy[i], array_titik),titik_menjadi_indeks(hasil_convex_hull_atas_as_numpy[i+1], array_titik)]]

    for i in range(len(hasil_convex_hull_bawah_as_numpy) - 1):
        return_value_bawah = return_value_bawah + [[titik_menjadi_indeks(hasil_convex_hull_bawah_as_numpy[i], array_titik),titik_menjadi_indeks(hasil_convex_hull_bawah_as_numpy[i+1], array_titik)]]

    return return_value_atas + return_value_bawah