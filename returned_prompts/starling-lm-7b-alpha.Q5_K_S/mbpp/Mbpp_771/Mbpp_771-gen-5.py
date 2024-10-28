
def check_expression(expr:str) -> bool:
  stack = []
  for char in expr:
    if char in ['(', '[', '{']:
      stack.append(char)
    elif char in [')', ']', '}']:
      if len(stack) == 0:
        return False
      top_char = stack.pop()
      if (char == ')' and top_char != '(') or (char == ']' and top_char != '[') or (char == '}' and top_char != '{'):
        return False
  return len(stack) == 0


