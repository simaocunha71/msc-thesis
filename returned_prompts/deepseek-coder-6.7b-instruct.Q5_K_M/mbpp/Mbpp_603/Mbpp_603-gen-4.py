
def get_ludic(n: int) -> list:
  return [i for i in range(1, n+1) if all(i % j != 0 for j in range(2, int(i**0.5)+1))]


