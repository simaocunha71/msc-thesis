def multiply_elements(t_1_Nplus1):
    return tuple(t_i * t_i_plus_1 for i, t_i in enumerate(t_1_Nplus1) for i_plus_1, t_i_plus_1 in zip(t_1_Nplus1[1:], t_1_Nplus1[1:]))