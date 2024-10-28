def move_num(s):
  nums = set('0123456789')
  res = ''
  num_str = ''
  for char in s:
    if char in nums:
      num_str += char
    else:
      if num_str:
        res += num_str
        num_str = ''
      res += char
  if num_str:
    res += num_str
  return res