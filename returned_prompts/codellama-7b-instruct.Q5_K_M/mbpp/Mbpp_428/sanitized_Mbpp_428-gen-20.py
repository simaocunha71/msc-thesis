def shell_sort(arr):
  n = len(arr)
  gap = int(n/2)
  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i - gap
      while j >= 0 and arr[j] > temp:
        arr[j + gap] = arr[j]
        j -= gap
      arr[j + gap] = temp
    gap = int(gap/2)
  return arr