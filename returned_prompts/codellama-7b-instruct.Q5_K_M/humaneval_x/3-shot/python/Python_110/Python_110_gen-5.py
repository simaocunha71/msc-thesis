    even = []

    for num in lst1:
        if num % 2 == 0:
            even.append(num)

    if len(even) == len(lst1):
        return "YES"

    for num in lst2:
        if num % 2 == 0:
            even.append(num)

    if len(even) == len(lst1):
        return "YES"

    return "NO"


