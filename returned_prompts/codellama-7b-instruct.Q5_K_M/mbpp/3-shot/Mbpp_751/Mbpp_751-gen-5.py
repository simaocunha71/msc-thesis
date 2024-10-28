
def check_min_heap(arr):
  n = len(arr)

  def is_min_heap(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    if l >= n and r >= n:
      return True

    if arr[i] > arr[l] or arr[i] > arr[r]:
      return False

    return is_min_heap(arr, l, n) and is_min_heap(arr, r, n)

  return is_min_heap(arr, 0, n)


