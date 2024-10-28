    def number_of_ones(n):
        count = 0
        while n:
            count += n % 2
            n //= 2
        return count

    return sorted(arr, key=lambda x: (number_of_ones(x), x))