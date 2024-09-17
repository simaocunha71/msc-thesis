
def check_expression(expression: str) -> bool:
  stack = []
  for char in expression:
    if char in ["(", "{", "["]:
      stack.append(char)
    elif char in [")", "}", "]"]:
      if len(stack) == 0:
        return False
      top = stack.pop()
      if not match(top, char):
        return False
  return len(stack) == 0


def match(open, close):
  return {"(": ")", "{": "}", "[": "]"}[open] == close


