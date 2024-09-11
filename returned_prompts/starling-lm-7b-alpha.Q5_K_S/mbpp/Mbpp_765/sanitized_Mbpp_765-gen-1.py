def is_polite(num):
    if num == 1:
        return 1
    elif num % 2 == 1:
        return num + is_polite(num - 1)
    else:
        return num + is_polite(num + 1)