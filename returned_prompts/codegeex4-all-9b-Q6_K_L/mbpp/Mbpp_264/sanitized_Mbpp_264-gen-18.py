def dog_age(n):
    if n < 0:
        return "Age cannot be negative"
    elif n == 0:
        return 0
    elif n == 1:
        return 15
    elif n == 2:
        return 24
    else:
        return 24 + (n - 2) * 4