def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        bell_numbers = [1, 1]
        for i in range(2, n+1):
            bell_numbers.append(sum(bell_numbers[:i]))
        return bell_numbers[-1]