
def find_kth(arr1, arr2, k):
  if k == 1:
    return min(arr1[0], arr2[0])

  i = min(len(arr1) - 1, k - 1)
  j = min(len(arr2) - 1, k - 1)

  if arr1[i] < arr2[j]:
    return arr1[i]
  else:
    return arr2[j]


