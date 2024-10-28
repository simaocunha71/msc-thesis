def move_zero(lst):
    left, right = 0, 0
    while right < len(lst):
        if lst[right] != 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
        right += 1
    return lst