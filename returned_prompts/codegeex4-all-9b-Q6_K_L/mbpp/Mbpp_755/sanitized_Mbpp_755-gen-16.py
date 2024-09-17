def second_smallest(numbers):
  smallest = second_smallest = float('inf')
  for n in numbers:
    if n < smallest:
      second_smallest = smallest
      smallest = n
    elif smallest < n < second_smallest:
      second_smallest = n
  return second_smallest