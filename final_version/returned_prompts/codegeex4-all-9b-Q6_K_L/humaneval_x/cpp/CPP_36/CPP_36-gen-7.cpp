def fizz_buzz(n):
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            for j in str(i):
                if j