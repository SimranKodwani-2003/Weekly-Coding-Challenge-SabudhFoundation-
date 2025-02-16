def max_prod(n):
  n.sort()

  max1=n[-1] *n[-2] *n[-3]
  triplet1=n[-1] ,n[-2] ,n[-3]

  max2=n[0] *n[1] *n[-1]
  triplet2=n[0],n[1],n[-1]

  if max1>max2:
    return triplet1
  else:
    return triplet2

n=[1, 7, 2, -2, 5]
max_prod(n)