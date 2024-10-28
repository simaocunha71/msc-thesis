def sum(num1: int, num2: int) -> int:
    return sum(set(range(1, min(num1, num2) + 1)) & set(range(num1, 0, -1)) & set(range(num2, 0, -1)))