def next_smallest_palindrome(n: int) -> int:
  n += 1
  while not is_palindrome(n):
    n += 1
  return n

def is_palindrome(n: int) -> bool:
  return str(n) == str(n)[::-1]

