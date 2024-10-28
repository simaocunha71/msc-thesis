    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
    # Or in one line:
    return any((balance := balance + operation) < 0 for operation in operations)


