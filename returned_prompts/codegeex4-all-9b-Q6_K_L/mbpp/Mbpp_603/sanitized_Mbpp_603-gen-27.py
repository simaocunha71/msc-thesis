def get_ludic(n):
  def is_ludic(num):
    if num < 2:
      return False
    for i in range(2, int(math.sqrt(num))+1):
      if num % i == 0:
        return False
    return True

  return [i for i in range(1, n+1) if is_ludic(i)]