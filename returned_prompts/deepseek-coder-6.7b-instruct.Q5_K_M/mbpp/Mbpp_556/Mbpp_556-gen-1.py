
def find_Odd_Pair(lst: list, n: int) -> int:
  count = 0
  for i in range(n):
    for j in range(i + 1, n):
      if (lst[i] ^ lst[j]) & 1:
        count += 1
  return count
"""
This function works by iterating over all pairs in the list and checking if their XOR is odd. If it is, it increments the count. The XOR operator '^' is used to find the XOR of the two numbers. The bitwise AND operator '&' is used to check if the XOR result is odd or not. If it is odd, the result of the bitwise AND operation will be 1, else 0.
"""

