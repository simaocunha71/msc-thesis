def is_Sum_Of_Powers_Of_Two(n: int) -> bool:
  return n == 2**int(math.log2(n)) if n != 0 else False