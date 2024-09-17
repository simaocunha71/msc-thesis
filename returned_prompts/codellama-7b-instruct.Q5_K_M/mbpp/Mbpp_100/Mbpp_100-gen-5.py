
def next_smallest_palindrome(n: int) -> int:
  is_palindrome = str(n) == str(n)[::-1]
  if is_palindrome:
    return n + 1
  else:
    str_num = str(n)
    left_half = str_num[:len(str_num)//2]
    right_half = str_num[len(str_num)//2:][::-1]
    return int(left_half + right_half)


