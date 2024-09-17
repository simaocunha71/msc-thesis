def is_Sub_Array(s1: list,s2: list) -> bool:
    for i in range(len(s1)):
        if s1[i] in s2:
            return True
    return False