
def round_and_sum(numbers: list) -> int:
  total = 0
  for num in numbers:
    total += round(num)
  return total * len(numbers)


