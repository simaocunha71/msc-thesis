
def next_smallest_palindrome(n):
  n = n + 1
  while str(n) != str(n)[::-1]:
    n += 1
  return n


