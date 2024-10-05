    def count_ones(n):
        count = 0
        while n > 0:
            count += n % 2
            n //= 2
        return count

    return sorted(arr, key=lambda x: (count_ones(x), x))