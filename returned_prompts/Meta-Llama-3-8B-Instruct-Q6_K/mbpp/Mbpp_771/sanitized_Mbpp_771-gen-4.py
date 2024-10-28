def check_expression(expression):
  stack = []
  for char in expression:
    if char in ['(', '[', '{']:
      stack.append(char)
    elif char in [')', ']', '}']:
      if not stack:
        return False
      top = stack.pop()
      if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
        return False
  return not stack