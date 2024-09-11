def is_majority(sorted_array: list, n: int, element: int) -> bool:
    count = 0
    for i in range(n):
        if sorted_array[i] == element:
            count += 1
    return count > n//2