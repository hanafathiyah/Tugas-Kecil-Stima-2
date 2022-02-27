# Nama  : Hana Fathiyah
# NIM   : 13520047
# Kelas : K02

import numpy as np

def myConvexHull(bucket):
  quicksort(bucket)
  print(bucket)


def quicksort(bucket):
  i = 0
  j = bucket.shape[0]
  k = bucket.shape[0]//2
  if (i < j):
    partisi(bucket,i,j,k)
    quicksort(bucket,i,k)
    quicksort(bucket,k+1,j)

def partisi(bucket,i,j,q):
  pivot = bucket.shape[0]//2
  p = i
  q = j
  while (p <= q):
    while (bucket[p][0] < pivot):
      p += 1
    while(bucket[q][0] > pivot):
      q -= 1
    if (p <= q):
      tmp_x = bucket[p][0]
      tmp_y = bucket[p][1]
      bucket[p][0] = bucket[q][0]
      bucket[p][1] = bucket[q][1]
      bucket[q][0] = tmp_x
      bucket[q][1] = tmp_y
      p += 1
      q -= 1
           



