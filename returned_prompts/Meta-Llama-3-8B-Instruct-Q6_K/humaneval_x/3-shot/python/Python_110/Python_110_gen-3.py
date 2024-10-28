    for num in lst1:
        if num % 2 != 0:
            if not any(num % 2 == 0 for num in lst2):
                return "NO"
            else:
                lst2.remove(next(num2 for num2 in lst2 if num2 % 2 == 0))
    return "YES"


