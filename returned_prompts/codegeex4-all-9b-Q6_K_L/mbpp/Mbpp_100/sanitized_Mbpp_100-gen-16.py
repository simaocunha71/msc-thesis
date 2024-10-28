def next_smallest_palindrome(num: int) -> int:
  if num < 10:
    return num + 1
  str_num = str(num)
  str_num_len = len(str_num)
  mid = str_num_len // 2
  left_half = str_num[:mid]
  right_half = str_num[mid + (1 if str_num_len % 2 else 0):]
  if str_num_len % 2:
    new_right_half = left_half[::-1]
  else:
    new_right_half = left_half[::-1][1:]
  new_num = int(left_half + new_right_half)
  while not str(new_num)[::-1] == str_num:
    new_num -= 1
  return new_num