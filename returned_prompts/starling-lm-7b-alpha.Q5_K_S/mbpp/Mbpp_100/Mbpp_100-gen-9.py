
def next_smallest_palindrome(n: int):
  if n % 11 == 0:
    return n + 10
  else:
    if (n + 11) % 11 == 0:
      return (n + 11) // 11 * 11
    else:
      return (n + 11) // 11 * 11 + 11


