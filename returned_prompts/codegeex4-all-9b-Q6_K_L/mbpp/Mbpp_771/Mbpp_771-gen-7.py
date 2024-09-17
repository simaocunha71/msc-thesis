def check_expression(expression: str) -> bool:
  stack = []
  for char in expression:
    if char in ["{", "[", "("]:
      stack.append(char)
    elif char in ["}", "]", ")"]:
      if not stack:
        return False
      last_open = stack.pop()
      if (last_open == "{" and char != "}") or (last_open == "[" and char != "]") or (last_open == "(" and char != ")"):
        return False
  return not stack

