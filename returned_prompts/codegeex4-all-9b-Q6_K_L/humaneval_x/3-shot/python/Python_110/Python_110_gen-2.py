    even_count = 0
    odd_count = 0

    for num in lst1:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    for num in lst2:
        if num % 2 == 0:
            even_count += 1

    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"

