def multiply_elements(t):
  return tuple(t[i]*t[i+1] for i in range(len(t)-1))