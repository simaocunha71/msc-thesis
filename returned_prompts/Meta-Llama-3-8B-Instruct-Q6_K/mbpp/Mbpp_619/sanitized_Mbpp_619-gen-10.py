def move_num(s):
  return ''.join(filter(str.isalpha, s)) + ''.join(filter(str.isdigit, s))  # or s.translate(str.maketrans("0123456789", ""))