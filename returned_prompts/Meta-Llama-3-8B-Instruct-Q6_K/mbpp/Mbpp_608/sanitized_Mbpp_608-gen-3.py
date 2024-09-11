def bell_Number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        bell_nums = [1, 2]
        for i in range(2, n):
            bell_nums.append(bell_nums[i-1] + sum(bell_nums[:i]))
        return bell_nums[-1]  # return the nth bell number