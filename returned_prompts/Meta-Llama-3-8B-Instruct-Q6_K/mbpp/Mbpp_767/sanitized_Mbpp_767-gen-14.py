def get_pairs_count(lst, sum):
    lst.sort()
    count = 0
    left = 0
    right = len(lst) - 1
    while left < right:
        current_sum = lst[left] + lst[right]
        if current_sum == sum:
            count += 1
            left += 1
            right -= 1
        elif current_sum < sum:
            left += 1
        else:
            right -= 1
    return count * 2