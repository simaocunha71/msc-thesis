def max_Product(arr: list) -> tuple:
  max_prod = 1
  imax = 0
  jmax = 0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      prod = arr[i] * arr[j]
      if prod > max_prod:
        max_prod = prod
        imax = i
        jmax = j
  return (arr[imax], arr[jmax])