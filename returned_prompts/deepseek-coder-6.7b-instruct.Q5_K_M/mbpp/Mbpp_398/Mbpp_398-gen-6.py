
def sum_of_digits(numbers):
  return sum(map(sum, map(digits, numbers)))

def digits(n):
  return [int(i) for i in str(n)]


