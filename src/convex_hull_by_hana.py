import numpy as np

def myConvexHull(array_titik):
    if len(array_titik) <= 2:
        return array_titik

  # membuat array kosong untuk convex hull (menyimpan dalam bentuk titik)
    hasil_convex_hull = []

    urutan_x = sorted(array_titik, key=lambda x: x[0])
    titik1 = urutan_x[0] # Titik minimum
    titik2 = urutan_x[-1] # Titik maksimum

    idx_titik1 = titik_menjadi_indeks(titik1, array_titik)
    idx_titik2 = titik_menjadi_indeks(titik2, array_titik)

    hasil_convex_hull = hasil_convex_hull + [titik1, titik2]

  # menghapus dari list setelah dimasukkan ke dalam proses convex hull
    urutan_x.pop(0)
    urutan_x.pop(-1)

  #  dnc pertama, membagi 2 area menjadi atas_garis dan bawah_garis
    atas_garis, bawah_garis = membuat_area(titik1, titik2, urutan_x)
    hasil_convex_hull = hasil_convex_hull + convex_hull_2(titik1, titik2, atas_garis, "atas")
    hasil_convex_hull = hasil_convex_hull + convex_hull_2(titik1, titik2, bawah_garis, "bawah")

    hasil_convex_hull = sorted(hasil_convex_hull, key=lambda x: x[0])

    hasil_convex_hull_as_numpy = membuat_tipe_numpy(hasil_convex_hull)

    return_value = []
    for i in range(len(hasil_convex_hull_as_numpy) - 1):
        return_value = return_value + [[titik_menjadi_indeks(hasil_convex_hull_as_numpy[i], array_titik),titik_menjadi_indeks(hasil_convex_hull_as_numpy[i+1], array_titik)]]

    atas_garis_as_numpy = membuat_tipe_numpy(atas_garis)
    bawah_garis_as_numpy = membuat_tipe_numpy(bawah_garis)
    return return_value, hasil_convex_hull_as_numpy, atas_garis_as_numpy, bawah_garis_as_numpy

def membuat_area(titik1, titik2, array_titik):

    area_atas = []
    area_bawah = []

    # kemungkinan 1: garis vertikal sehingga di atas dan di bawah garis tidak ada titik
    if (titik1[0] == titik2[0]):
        return area_atas, area_bawah

    # mencari kemiringan dan titik potong sumbu-y dengan y = mx + c
    # m = (y2 - y1)/(x2 - x1)
    m = (titik2[1] - titik1[1]) /(titik2[0] - titik1[0])
    # c = - mx + y
    c = -1 * m * titik1[0] + titik1[1]

    for sumbu in array_titik:
        # deteksi letak suatu titik
        if (sumbu[1] > m * (sumbu[0]) + c): 
            # titik di atas garis
            area_atas.append(sumbu)
        elif (sumbu[1] < m * (sumbu[0]) + c): 
            # titik di bawah garis
            area_bawah.append(sumbu)
    
    return area_atas, area_bawah

def membuat_tipe_numpy(elemen):
    hasil = np.array(elemen)
    return hasil

def convex_hull_2(titik1, titik2, area, area_titik):

    # mengecek apakah salah satu dari ketiga elemen tersebut kosong atau tidak
    if (area == [] or titik1 is None or titik2 is None):
        return []

    convex_hull_baru = []

    # menghitung jarak setiap titik dari garis dan mencari titik dengan jarak terjauh
    jarak_terjauh = -1
    titik_terjauh = None

    indeks_titik = 0
    indeks_titik_terjauh = -1
    for titik in area:
        jarak_titik_i_ke_garis = jarak_titik_ke_garis(titik1, titik2, titik)
        if (jarak_titik_i_ke_garis > jarak_terjauh):
            jarak_terjauh = jarak_titik_i_ke_garis
            titik_terjauh = titik
            indeks_titik_terjauh = indeks_titik
        indeks_titik += 1;

    convex_hull_baru = convex_hull_baru + [titik_terjauh]

    # menghapus titik terjauh yang sudah terdata
    # area.delete(titik_terjauh)
    np.delete(area, indeks_titik_terjauh)

    # membuat area
    titik1atas, titik1bawah = membuat_area(titik1, titik_terjauh, area)
    titik2atas, titik2bawah = membuat_area(titik2, titik_terjauh, area)
    '''
    if area_titik == "atas":
        convex_a = convex_hull_2(titik1, titik_terjauh, titik1atas, "atas")
        convex_b = convex_hull_2(titik_terjauh, titik2, titik2atas, "atas")
        convex_hull_baru = convex_hull_baru + convex_a
        convex_hull_baru = convex_hull_baru + convex_b
    else:
        convex_c = convex_hull_2(titik1, titik_terjauh, titik1bawah, "bawah")
        convex_d = convex_hull_2(titik_terjauh, titik2, titik2bawah, "bawah")
        convex_hull_baru = convex_hull_baru + convex_c
        convex_hull_baru = convex_hull_baru + convex_d
    '''
    return convex_hull_baru

def jarak_titik_ke_garis(titik1, titik2, titik3):
  
    # dimisalkan suatu garis l terbentuk dari titik1 dan titik2
    # fungsi akan me-return jarak titik3 ke garis l tersebut

    # Ax + By + C = 0
    # (y - y1) = m(x - x1)
    # (y - y1)/(y2 - y1) = (x - x1)/(x2 - x1)

    A = titik1[1] - titik2[1]
    B = titik1[0] - titik2[0]
    C = titik1[0] * titik2[1] - titik2[0] * titik1[1]

    # rumus | Ax + By + C | / akar(A^2 + B^2)

    return abs(A*titik3[0] + B*titik3[1] + C) / ((A*A + B*B)**(1/2))

def titik_menjadi_indeks(titik, array_of_titik):
    for i in range(array_of_titik.shape[0]):
        if(titik[0] == array_of_titik[i][0] and titik[1] == array_of_titik[i][1]):
            return i