
def find_Rotations(s: str) -> int:
    return len(s) - len(set("".join(cyclic_rotations(s))))

def cyclic_rotations(s: str) -> list:
    return [s[i:] + s[:i] for i in range(len(s))]


