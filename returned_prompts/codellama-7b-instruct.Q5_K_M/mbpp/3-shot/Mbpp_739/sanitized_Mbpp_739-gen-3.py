def find_Index(n):
  count = 0
  index = 0
  while True:
    count += 1
    index += count
    if len(str(index)) == n:
      return index