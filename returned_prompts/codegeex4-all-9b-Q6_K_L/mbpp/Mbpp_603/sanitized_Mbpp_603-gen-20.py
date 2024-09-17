def get_ludic(n):
  def is_ludic(n):
    for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
        return False
    return True
  return [i for i in range(1, n+1) if is_ludic(i)]