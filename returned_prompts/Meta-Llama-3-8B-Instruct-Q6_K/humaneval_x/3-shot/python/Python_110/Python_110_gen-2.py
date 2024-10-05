    for num in lst1:
        if num % 2 != 0:
            if num not in lst2:
                return "NO"
            lst2.remove(num)
    return "YES"


