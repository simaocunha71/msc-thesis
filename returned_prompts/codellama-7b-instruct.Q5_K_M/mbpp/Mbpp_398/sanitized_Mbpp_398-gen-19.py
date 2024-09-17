def sum_of_digits(my_list):
  return [sum(int(digit) for digit in str(num)) for num in my_list]