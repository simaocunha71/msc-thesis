    def sum_of_four_evens(start):
        total = 0
        for _ in range(4):
            total += start
            start += 2
        return total

    return sum_of_four_evens(2) == n


