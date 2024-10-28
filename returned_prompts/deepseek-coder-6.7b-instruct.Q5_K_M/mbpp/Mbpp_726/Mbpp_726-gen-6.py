
def multiply_elements(numbers):
  return tuple(numbers[i] * numbers[i+1] for i in range(len(numbers)-1))


