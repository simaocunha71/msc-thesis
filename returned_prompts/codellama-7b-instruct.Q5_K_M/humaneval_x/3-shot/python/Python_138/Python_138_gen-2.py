    for i in range(1, n + 1):
        if i % 2 == 0:
            if n - i in range(1, n + 1):
                if n - i % 2 == 0:
                    return True
    return False


