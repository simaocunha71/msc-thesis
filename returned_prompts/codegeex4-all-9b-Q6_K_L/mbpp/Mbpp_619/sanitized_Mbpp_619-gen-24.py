def move_num(s: str) -> str:
    num_str = ''.join(filter(str.isdigit, s))
    alpha_str = ''.join(filter(str.isalpha, s))
    return alpha_str + num_str