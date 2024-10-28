def bell_Number(n):
    if n == 0:
        return 1
    bell_numbers = [0]*(n+1)
    bell_numbers[0] = 1
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            bell_numbers[i] += bell_numbers[j-1]
    return bell_numbers[n]