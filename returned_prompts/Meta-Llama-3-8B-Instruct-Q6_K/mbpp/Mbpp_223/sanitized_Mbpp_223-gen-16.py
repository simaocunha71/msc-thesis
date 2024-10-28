def is_majority(sorted_array, n, element):
    count = 0
    candidate = None
    for num in sorted_array:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return sorted_array.count(candidate) > n / 2