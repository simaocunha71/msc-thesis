
def mul_even_odd(nums:list)->int:
  even = list(filter(lambda x: x%2==0,nums))
  odd = list(filter(lambda x: x%2!=0,nums))
  if len(even)==0:
    return -1
  if len(odd)==0:
    return even[0]
  return even[0]*odd[0]


