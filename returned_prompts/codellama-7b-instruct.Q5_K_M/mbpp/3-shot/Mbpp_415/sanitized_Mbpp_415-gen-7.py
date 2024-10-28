def max_Product(arr: list) -> tuple:
  return max(zip(arr, arr[1:]), key=sum)