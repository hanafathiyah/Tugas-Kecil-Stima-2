def membuat_area(titik1, titik2, array_titik):

    area_atas = []
    area_bawah = []

    # kemungkinan 1: garis vertikal sehingga di atas dan di bawah garis tidak ada titik
    if (titik1[0] == titik2[0]):
        return area_atas, area_bawah

    # mencari kemiringan dan titik potong sumbu-y dengan y = mx + c
    # m = (y2 - y1)/(x2 - x1)
    m = (titik2[1] - titik1[1]) /(titik2[0] - titik1[0])