def find_Parity(n: int) -> bool:
    parity = sum(1 for i in range(n) if i % 2 == 0) % 2
    return parity == 0