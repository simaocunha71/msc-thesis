
def check_expression(s:str) -> bool:
  stack = []
  for char in s:
    if char == '(' or char == '{' or char == '[':
      stack.append(char)
    elif char == ')' or char == '}' or char == ']':
      if len(stack) == 0:
        return False
      elif stack[-1] == '(' and char != ')':
        return False
      elif stack[-1] == '{' and char != '}':
        return False
      elif stack[-1] == '[' and char != ']':
        return False
      else:
        stack.pop()
  if len(stack) == 0:
    return True
  else:
    return False


