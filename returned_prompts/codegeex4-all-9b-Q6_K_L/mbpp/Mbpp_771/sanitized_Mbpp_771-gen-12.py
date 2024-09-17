def check_expression(expression: str) -> bool:
  stack = []
  for char in expression:
    if char in ['{', '[', '(']:
      stack.append(char)
    else:
      if not stack:
        return False
      top = stack.pop()
      if char == '}' and top != '{':
        return False
      elif char == ']' and top != '[':
        return False
      elif char == ')' and top != '(':
        return False
  return not stack