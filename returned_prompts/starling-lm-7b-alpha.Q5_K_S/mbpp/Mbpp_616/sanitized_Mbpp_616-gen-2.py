def tuple_modulo(t1, t2):
    modulo_list = []
    for i in range(len(t1)):
        modulo_list.append(t1[i] % t2[i])
    return tuple(modulo_list)