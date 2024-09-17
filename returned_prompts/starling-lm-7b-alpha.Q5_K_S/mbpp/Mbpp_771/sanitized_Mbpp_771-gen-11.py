def check_expression(exp: str) -> bool:
  stack = []
  for c in exp:
    if c == "(":
      stack.append(c)
    elif c == ")":
      if len(stack) == 0:
        return False
      stack.pop()
    elif c == "{":
      stack.append(c)
    elif c == "}":
      if len(stack) == 0:
        return False
      stack.pop()
    elif c == "[":
      stack.append(c)
    elif c == "]":
      if len(stack) == 0:
        return False
      stack.pop()
  if len(stack) == 0:
    return True
  else:
    return False