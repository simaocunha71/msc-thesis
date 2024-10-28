def is_octagonal(n):
    octagonal_numbers = [0, 1, 6, 13, 28, 45, 70, 99, 130, 165, 200, 237, 276, 317, 360, 405, 452, 501, 552, 605, 660]
    if n <= len(octagonal_numbers):
        return octagonal_numbers[n-1]
    else:
        a = 1
        b = 2
        sum = 1
        count = 1
        while count < n:
            a, b = b, a + b + 1
            sum += a
            count += 1
        return sum