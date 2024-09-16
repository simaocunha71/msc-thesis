def find_star_num(n):
    if n <= 0:
        return None
    start = 1
    end = 10
    while n > 0:
        mid = (start + end) // 2
        if mid ** 2 > n:
            end = mid - 1
        else:
            start = mid + 1
    return end
