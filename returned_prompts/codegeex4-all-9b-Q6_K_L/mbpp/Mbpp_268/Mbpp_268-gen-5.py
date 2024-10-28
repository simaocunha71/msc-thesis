def find_star_num(n: int) -> int:
  def star_num(n: int) -> int:
    return n * (n + 1) // 2
  return star_num(n)

