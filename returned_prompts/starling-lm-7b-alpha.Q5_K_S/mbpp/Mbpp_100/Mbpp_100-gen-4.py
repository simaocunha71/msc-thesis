
def next_smallest_palindrome(n):
  if n % 2 == 0:
    n += 1
  if n % 5 == 0:
    n += 1
  while True:
    str_n = str(n)
    if str_n == str_n[::-1]:
      return n
    n += 1


