
def shell_sort(arr):
  n = len(arr)
  gaps = [701, 301, 132, 57, 23, 10, 4, 1]
  for gap in gaps:
      for i in range(gap, n):
          temp = arr[i]
          j = i
          while j >= gap and arr[j - gap] > temp:
              arr[j] = arr[j - gap]
              j -= gap
          arr[j] = temp
  return arr


