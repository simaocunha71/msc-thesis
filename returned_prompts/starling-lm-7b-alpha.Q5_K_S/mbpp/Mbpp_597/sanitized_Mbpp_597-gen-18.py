def find_kth(arr1: list, arr2: list, k: int) -> int:
  len_arr1 = len(arr1)
  len_arr2 = len(arr2)
  if len_arr1 > len_arr2:
    arr1, arr2 = arr2, arr1
    len_arr1, len_arr2 = len_arr2, len_arr1
  if k > len_arr1:
    return find_kth(arr1[:k-len_arr1], arr2, k-len_arr1)
  return max(find_kth(arr1[:k], arr2[:k], k),
             find_kth(arr1[:k]+arr1[k:len_arr1+k], arr2[k:len_arr2]+arr2[:k], k))