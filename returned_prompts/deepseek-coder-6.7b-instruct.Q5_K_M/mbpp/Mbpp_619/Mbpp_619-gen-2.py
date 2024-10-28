
def move_num(s):
  return ''.join(i for i in s if not i.isdigit()) + ''.join(i for i in s if i.isdigit())


