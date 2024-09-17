def toggle_middle_bits(n: int) -> int:
    n = bin(n)[2:]
    n_len = len(n)
    n_middle = n[1:n_len-1]
    n_middle = "".join(["1" if i == "0" else "0" for i in n_middle])
    return int(n[:1] + n_middle + n[-1], 2)