
def check_expression(exp:str):
  stack = []
  for char in exp:
    if char in "([{":
      stack.append(char)
    elif char in ")]}":
      if len(stack) == 0 or (char == ")" and stack[-1] != "["):
        return False
      else:
        stack.pop()
  return len(stack) == 0


