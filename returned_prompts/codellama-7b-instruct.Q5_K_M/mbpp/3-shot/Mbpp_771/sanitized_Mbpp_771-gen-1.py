def check_expression(expression):
  stack = []
  for char in expression:
    if char == "(":
      stack.append(")")
    elif char == "{":
      stack.append("}")
    elif char == "[":
      stack.append("]")
    elif char == stack[-1]:
      stack.pop()
    else:
      return False
  if not stack:
    return True
  else:
    return False