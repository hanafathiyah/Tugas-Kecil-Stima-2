import numpy as np

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

def membuat_area(titik1, titik2, array_titik):

    area_atas = []
    area_bawah = []

    # kemungkinan 1: garis vertikal sehingga di atas dan di bawah garis tidak ada titik
    if (titik1[0] == titik2[0]):
        return area_atas, area_bawah

    # mencari kemiringan dan titik potong sumbu-y dengan y = mx + c
    # m = (y2 - y1)/(x2 - x1)
    # m = (titik2[1] - titik1[1]) /(titik2[0] - titik1[0])
    # c = - mx + y
    # (y - y1) / (x2 - x1)
    # c = -1 * m * titik1[0] + titik1[1]

    for sumbu in array_titik:
        y = sumbu[1]
        x = sumbu[0]
        y2 = titik2[1]
        y1 = titik1[1]
        x2 = titik2[0]
        x1 = titik1[0]

        # deteksi letak suatu titik
        if (y - y1) * (x2 - x1) > (x - x1) * (y2 - y1):
            area_atas.append(sumbu)
        elif (y - y1) * (x2 - x1) < (x - x1) * (y2 - y1):
            area_bawah.append(sumbu) 

        '''
        if (sumbu[1] > m * (sumbu[0]) + c): 
            # titik di atas garis
            area_atas.append(sumbu)
        elif (sumbu[1] < m * (sumbu[0]) + c): 
            # titik di bawah garis
            area_bawah.append(sumbu)
        '''
    return area_atas, area_bawah

def membuat_tipe_numpy(elemen):
    hasil = np.array(elemen)
    return hasil

def fungsi_convex_hull(titik1, titik2, array_titik, posisi):
    if (len(array_titik) < 2):
        return array_titik

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
    # area.delete(titik_terjauh)
    #if atas_garis != []:
    np.delete(atas_garis, indeks_titik_terjauh)

    # membuat area
    titik1atas, titik1bawah = membuat_area(titik1, titik_terjauh, atas_garis)
    titik2atas, titik2bawah = membuat_area(titik_terjauh, titik2, atas_garis)

    convex_hull_atas = convex_hull_atas + fungsi_convex_hull_atas(titik1, titik_terjauh, titik1atas)
    convex_hull_atas = convex_hull_atas + fungsi_convex_hull_atas(titik_terjauh, titik2, titik2atas)

    return convex_hull_atas

def fungsi_convex_hull_bawah(titik1, titik2, bawah_garis):

    # mengecek apakah salah satu dari ketiga elemen tersebut kosong atau tidak
    if (bawah_garis == [] or titik1 is None or titik2 is None):
        return bawah_garis

    convex_hull_bawah = []

    # menghitung jarak setiap titik dari garis dan mencari titik dengan jarak terjauh
    jarak_terjauh = -1
    titik_terjauh = None

    indeks_titik = 0
    indeks_titik_terjauh = -1

    for titik in bawah_garis:
        jarak_titik_i_ke_garis = jarak_titik_ke_garis(titik1, titik2, titik)
        if (jarak_titik_i_ke_garis > jarak_terjauh):
            jarak_terjauh = jarak_titik_i_ke_garis
            titik_terjauh = titik
            indeks_titik_terjauh = indeks_titik
        indeks_titik += 1

    convex_hull_bawah = convex_hull_bawah + [titik_terjauh]

    # menghapus titik terjauh yang sudah terdata
    # area.delete(titik_terjauh)
    np.delete(bawah_garis, indeks_titik_terjauh)

    # membuat area
    titik1atas, titik1bawah = membuat_area(titik1, titik_terjauh, bawah_garis)
    titik2atas, titik2bawah = membuat_area(titik_terjauh, titik2, bawah_garis)

    convex_hull_bawah = convex_hull_bawah + fungsi_convex_hull_bawah(titik1, titik_terjauh, titik1bawah)
    convex_hull_bawah = convex_hull_bawah + fungsi_convex_hull_bawah(titik_terjauh, titik2, titik2bawah)

    return convex_hull_bawah

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

def titik_menjadi_indeks(titik, array_of_titik):
    for i in range(len(array_of_titik)):
        if(titik[0] == array_of_titik[i][0] and titik[1] == array_of_titik[i][1]):
            return i

def jarak_titik_ke_titik(titik1, titik2):
    return np.sqrt((titik1[0] - titik2[0]) ** 2 + (titik1[1] - titik2[1]) ** 2) 