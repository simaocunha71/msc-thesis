    even_sum = sum(filter(lambda x: x % 2 == 0, lst1))
    odd_sum = sum(filter(lambda x: x % 2 != 0, lst1))
    odd_sum2 = sum(filter(lambda x: x % 2 != 0, lst2))

    if even_sum == 0:
        return "NO"
    if even_sum == odd_sum + odd_sum2:
        return "YES"

    return "NO"


