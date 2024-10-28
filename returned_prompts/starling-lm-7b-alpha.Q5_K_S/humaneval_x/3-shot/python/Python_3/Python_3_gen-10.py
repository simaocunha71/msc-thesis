    balance = 0
    for elem in operations:
        balance += elem
        if balance < 0:
            return True

    return False


