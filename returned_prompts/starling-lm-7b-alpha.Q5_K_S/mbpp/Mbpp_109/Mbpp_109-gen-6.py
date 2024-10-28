
def odd_Equivalent(s:str, rotate:int) -> int:
  return len([i for i in s if int(i) % 2 != 0])


