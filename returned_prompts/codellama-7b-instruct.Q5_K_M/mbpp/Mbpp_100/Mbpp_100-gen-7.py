
def next_smallest_palindrome(n: int) -> int:
  temp = str(n)
  temp = temp[::-1]
  if temp == temp[::-1]:
    return int(temp) + 1
  else:
    return int(str(int(temp)+1)[::-1])


