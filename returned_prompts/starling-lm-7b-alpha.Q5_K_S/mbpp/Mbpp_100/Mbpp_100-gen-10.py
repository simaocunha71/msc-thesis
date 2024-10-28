
def next_smallest_palindrome(num: int) -> int:
  while True:
    if str(num) == str(num)[::-1]:
      return num
    num += 1


