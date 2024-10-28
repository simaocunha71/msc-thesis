def sum_Of_Subarray_Prod(lst: list) -> int:
  result = 0
  for i in range(len(lst)):
    for j in range(i+1, len(lst)+1):
      subarray = lst[i:j]
      product = 1
      for num in subarray:
        product *= num
      result += product
  return result