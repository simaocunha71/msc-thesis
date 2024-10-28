def next_smallest_palindrome(n: int) -> int:
  n = str(n)
  if n == n[::-1]:
    return int(n) + 1
  else:
    n = n[::-1]
    n = str(int(n) + 1)
    n = n[::-1]
    return int(n)