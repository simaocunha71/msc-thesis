def get_ludic(n):
  def is_ludic(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))

  return [i for i in range(1, n+1) if is_ludic(i)]