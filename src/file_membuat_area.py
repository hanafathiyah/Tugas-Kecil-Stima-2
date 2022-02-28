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

    return area_atas, area_bawah