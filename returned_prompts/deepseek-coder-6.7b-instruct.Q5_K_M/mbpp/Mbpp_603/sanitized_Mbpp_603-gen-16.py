def get_ludic(n):
  def is_ludic(num):
    if num == 1:
      return True
    if num % 2 != 0:
      return False
    while num % 2 == 0:
      num = num / 2
    return num == 1
  return [i for i in range(1, n+1) if is_ludic(i)]