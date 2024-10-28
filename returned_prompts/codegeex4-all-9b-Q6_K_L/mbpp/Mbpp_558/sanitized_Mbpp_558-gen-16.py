def digit_distance_nums(n1, n2):
  if n1 == n2:
    return 0
  n1_digits = [int(digit) for digit in str(n1)]
  n2_digits = [int(digit) for digit in str(n2)]
  digit_diff = [abs(d1 - d2) for d1, d2 in zip(n1_digits, n2_digits)]
  return sum(digit_diff)