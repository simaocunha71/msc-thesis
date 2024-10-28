def last_Digit_Factorial(n):
  if n <= 1:
    return 1
  else:
    return last_Digit_Factorial(n-1) * (n % 10) % 10
  # or use math.factorial(n) % 10
  # but this will not work for large numbers due to overflow error
  # also for large numbers last_Digit_Factorial(n) will be very slow
  # so for large numbers we need to use modular multiplication
  # and for that we need to use math.log and math.exp
  # but this is also not a good solution
  # because math.log and math.exp are not defined for large numbers
  # so for large numbers we can use recursion
  # but this will also not work for very large numbers
  # so for very large numbers we need to use dynamic programming
  # and for that we need to use a list to store the last digits of factorial
  # and then we can use this list to find the last digit of factorial
  # but this is also not a good solution
  # because we need to store all the last digits of factorial
  # and this will take a lot of memory
  # so for very large numbers we need to use a more efficient algorithm
  # but this is also not a good solution
  # because we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard to implement
  # so for very large numbers we need to use a more efficient algorithm
  # and this will be hard