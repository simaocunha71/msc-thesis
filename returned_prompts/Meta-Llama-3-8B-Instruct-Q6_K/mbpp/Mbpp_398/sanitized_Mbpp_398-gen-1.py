def sum_of_digits(nums):
  return sum(sum(int(digit) for digit in str(num)) for num in nums)  # Python 3.9 and later
  # return sum(sum(int(digit) for digit in str(num)) for num in nums).sum()  # Python 3.7 and earlier