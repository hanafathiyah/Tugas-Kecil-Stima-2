# Nama  : Hana Fathiyah
# NIM   : 13520047
# Kelas : K02

from area import membuat_area
from convex_hull_2 import convex_hull_2
from titik_menjadi_indeks import titik_menjadi_indeks

def myConvexHull(array_titik):
  # if len(array_titik) <= 2:
  #  return titik_menjadi_indeks(array_titik)

  # membuat array kosong untuk convex hull
  hasil_convex_hull = []

  urutan_x = sorted(array_titik, key=lambda x: (x[0],x[1]))
  titik1 = urutan_x[0] # Titik minimum
  titik2 = urutan_x[-1] # Titik maksimum

  hasil_convex_hull = hasil_convex_hull + [titik1, titik2]

  # menghapus dari list setelah dimasukkan ke dalam proses convex hull
  urutan_x.pop(0)
  urutan_x.pop(-1)

  atas_garis, bawah_garis = membuat_area(titik1, titik2, urutan_x)
  hasil_convex_hull = hasil_convex_hull + convex_hull_2(titik1, titik2, atas_garis, "atas")
  hasil_convex_hull = hasil_convex_hull + convex_hull_2(titik1, titik2, bawah_garis, "bawah")

  return_value = []

  for hasil in hasil_convex_hull:
    return_value = return_value + [titik_menjadi_indeks(hasil[0], hasil[1], array_titik), titik_menjadi_indeks(hasil[2], hasil[3], array_titik)]
  
  return return_value