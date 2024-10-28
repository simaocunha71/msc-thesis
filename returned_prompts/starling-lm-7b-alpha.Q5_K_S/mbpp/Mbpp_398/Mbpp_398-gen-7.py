
def sum_of_digits(nums:list)->int:
  total_sum = 0
  for num in nums:
    total_sum += sum(int(digit) for digit in str(num))
  return total_sum


