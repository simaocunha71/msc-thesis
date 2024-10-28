def is_majority(sorted_array, n, element):
    if n % 2 != 0:
        return False
    count = 0
    for i in range(n):
        if sorted_array[i] == element:
            count += 1
    return count > n // 2