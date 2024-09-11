def sum_of_digits(lst):
  return sum(sum(map(int, str(num))) for num in lst)  # or return sum(sum(int(digit) for digit in str(num)) for num in lst) if python version is less than 3.9