def odd_Equivalent(s, k):
  # Convert binary string to integer
  num = int(s, 2)
  # Calculate the number of times the binary string is rotated
  for i in range(k):
    # Rotate the binary string
    num = (num << 1) | (num >> (len(s) - 1))
    # Convert the rotated binary string to integer
    num = int(bin(num)[2:])
  # Count the number of odd numbers
  count = 0
  while num:
      num, r = divmod(num, 2)
      count += r
  return count