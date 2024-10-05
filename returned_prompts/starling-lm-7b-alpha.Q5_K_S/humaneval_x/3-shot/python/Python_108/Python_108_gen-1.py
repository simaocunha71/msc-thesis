    def sum_of_digits(n):
        return sum(map(int, str(abs(n))))

    count = 0
    for x in arr:
        if sum_of_digits(x) > 0:
            count += 1

    return count


