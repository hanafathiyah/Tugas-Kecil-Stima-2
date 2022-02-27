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

