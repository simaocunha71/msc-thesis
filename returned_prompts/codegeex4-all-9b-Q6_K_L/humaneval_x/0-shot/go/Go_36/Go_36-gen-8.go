def FizzBuzz(n):
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            s = str(i)
            count += s.count('7')
    return count

