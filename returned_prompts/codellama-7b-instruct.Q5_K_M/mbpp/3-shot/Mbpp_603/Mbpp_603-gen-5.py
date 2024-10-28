
def get_ludic(limit:int) -> list:
  ludic_nums = []
  for i in range(2,limit+1):
    if all(i%j for j in range(2,i)):
      ludic_nums.append(i)
  return ludic_nums


