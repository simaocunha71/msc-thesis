def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True