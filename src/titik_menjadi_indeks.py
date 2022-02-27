from hashlib import sha1
from turtle import shape


def titik_menjadi_indeks(titik_x, titik_y, array_of_titik):
    for i in range(array_of_titik.shape[0]):
        for j in range(array_of_titik.shape[1]):
            if(titik_x == array_of_titik[i] and titik_y == array_of_titik[j]):
                return i,j;