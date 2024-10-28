
def check(num):
  reverse = int(str(num)[::-1])
  twice_less = reverse - 1
  return num == twice_less * 2


