def check_expression(expr):
  stack = []
  opening = ['[', '{', '('] 
  closing = [']', '}', ')'] 
  for i in expr:
    if i in opening:
      stack.append(i)
    elif i in closing:
      pos = closing.index(i)
      if ((len(stack) > 0) and (opening[pos] == stack[len(stack)-1])): 
        stack.pop()
      else: 
        return False
  if len(stack) == 0:
    return True
  else:
    return False