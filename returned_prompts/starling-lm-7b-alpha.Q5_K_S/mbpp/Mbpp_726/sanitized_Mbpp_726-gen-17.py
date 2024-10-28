def multiply_elements(t_1: tuple) -> tuple:
  result = ()
  for i in range(len(t_1)-1):
    result = result + (t_1[i]*t_1[i+1],)
  return result