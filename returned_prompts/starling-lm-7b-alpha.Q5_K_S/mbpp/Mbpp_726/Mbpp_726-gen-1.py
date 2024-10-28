
def multiply_elements(t_1_Nplus1: tuple) -> tuple:
  return tuple(t_i * (t_i + 1) for i in range(len(t_1_Nplus1)-1))


