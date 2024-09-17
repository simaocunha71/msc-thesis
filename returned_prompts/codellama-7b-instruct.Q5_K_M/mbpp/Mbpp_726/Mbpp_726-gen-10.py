
def multiply_elements(t: tuple) -> tuple:
  t_multiplied = []
  for i in range(len(t)-1):
    t_multiplied.append(t[i] * t[i+1])
  return tuple(t_multiplied)


