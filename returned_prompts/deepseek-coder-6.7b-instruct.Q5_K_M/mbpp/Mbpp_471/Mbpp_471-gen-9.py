
def find_remainder(arr,n):
  product = 1
  for i in arr:
    product = (product * i) % n
  return product % n


