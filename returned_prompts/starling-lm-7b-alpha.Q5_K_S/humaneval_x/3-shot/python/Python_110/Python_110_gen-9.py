    odd_count = 0
    even_count = 0
    for elem in lst1:
        if elem % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count == 0:
        return "YES"

    for elem in lst2:
        if elem % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

            if odd_count == odd_count:
                return "NO"

    return "YES"


