    for num in lst1:
        if num % 2 != 0:
            if not any(num % 2 == 0 for num in lst2):
                return "NO"
            lst2.remove(next(num for num in lst2 if num % 2 == 0))
    return "YES"
