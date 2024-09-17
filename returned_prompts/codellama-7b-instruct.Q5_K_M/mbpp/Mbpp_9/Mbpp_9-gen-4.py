
def find_Rotations(strng: str) -> int:
  if len(strng) == 1:
    return 0
  else:
    if strng == strng[::-1]:
      return 1
    else:
      for i in range(len(strng)-1):
        if strng[:-i] == strng[i:]:
          return len(strng) - i


