def odd_Equivalent(binary_string: str, rotations: int) -> int:
    binary_string *= rotations
    return sum(binary_string[i] != binary_string[i - 1] for i in range(1, len(binary_string)))