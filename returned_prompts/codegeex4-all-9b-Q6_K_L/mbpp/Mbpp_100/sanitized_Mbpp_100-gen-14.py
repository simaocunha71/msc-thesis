def next_smallest_palindrome(n):
  if n < 10:
    return n+1
  s = str(n)
  l = len(s)
  if l % 2 == 0:
    l1 = s[:l//2]
    l2 = s[l//2:]
    l3 = l1 + l2[::-1]
    if int(l3) == n:
      l1 = str(int(l1)-1)
      l3 = l1 + l2[::-1]
      return int(l3)
    else:
      return int(l3)
  else:
    l1 = s[:l//2+1]
    l2 = s[l//2+1:]
    l3 = l1 + l2[::-1]
    if int(l3) == n:
      l1 = str(int(l1)-1)
      l3 = l1 + l2[::-1]
      return int(l3)
    else:
      return int(l3)