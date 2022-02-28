def titik_menjadi_indeks(titik, array_of_titik):
    for i in range(len(array_of_titik)):
        if(titik[0] == array_of_titik[i][0] and titik[1] == array_of_titik[i][1]):
            return i