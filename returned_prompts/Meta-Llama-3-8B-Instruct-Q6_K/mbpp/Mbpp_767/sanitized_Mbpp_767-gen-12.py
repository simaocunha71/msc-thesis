def get_pairs_count(lst, sum):
    lst.sort()
    left, right = 0, len(lst) - 1
    count = 0
    while left < right:
        total = lst[left] + lst[right]
        if total == sum:
            count += 1
            left += 1
            right -= 1
        elif total < sum:
            left += 1
        else:
            right -= 1
    return count * 2