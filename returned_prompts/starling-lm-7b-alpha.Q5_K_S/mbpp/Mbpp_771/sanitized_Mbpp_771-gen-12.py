def check_expression(expression: str) -> bool:
  stack = []
  for char in expression:
    if char in ["(", "{", "["]:
      stack.append(char)
    elif char in [")", "}", "]"]:
      if len(stack) == 0:
        return False
      elif char == ")" and stack[-1] != "(":
        return False
      elif char == "}" and stack[-1] != "{":
        return False
      elif char == "]" and stack[-1] != "[":
        return False
      else:
        stack.pop()
  return len(stack) == 0