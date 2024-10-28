
def next_smallest_palindrome(num):
  num = str(num)
  l = len(num)
  if l == 1:
    return int(num) + 1
  if l % 2 == 0:
    mid = l // 2
  else:
    mid = l // 2 + 1
  left = num[:mid]
  right = num[mid:]
  if left == right[::-1]:
    right = str(int(right) + 1)
    return int(left + right[::-1])
  else:
    right = str(int(right) + 1)
    return int(left + right[::-1])


