def move_num(s: str) -> str:
  numbers = []
  for i in s:
    if i.isdigit():
      numbers.append(i)
  for i in s:
    if i not in numbers:
      print(i,end='')
  for i in numbers:
    print(i,end='')
  return ""