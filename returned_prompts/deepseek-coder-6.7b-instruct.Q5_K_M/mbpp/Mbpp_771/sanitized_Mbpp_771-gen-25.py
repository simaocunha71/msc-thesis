def check_expression(expr):
  stack = []
  balanced = True
  open_brackets = ['(', '[', '{']
  close_brackets = [')', ']', '}']

  for bracket in expr:
    if bracket in open_brackets:
      stack.append(bracket)
    elif bracket in close_brackets:
      pos = close_brackets.index(bracket)
      if ((len(stack) > 0) and (open_brackets[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        balanced = False
        break
  if len(stack) == 0:
    return balanced
  return False