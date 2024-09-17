
def comb_sort(arr):
  n = len(arr)
  gap = n
  swapped = True
  while (gap > 1 or swapped == True):
    gap = int(gap / 1.247330950103979)
    swapped = False
    for i in range(n - gap):
      if arr[i] < arr[i + gap]:
        arr[i], arr[i + gap] = arr[i + gap], arr[i]
        swapped = True
  return arr


