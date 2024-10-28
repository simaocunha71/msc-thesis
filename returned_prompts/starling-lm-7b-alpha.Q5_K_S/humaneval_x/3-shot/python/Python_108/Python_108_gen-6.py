    def num_sum(x):
        return sum(map(int, str(abs(x))))

    return sum(map(num_sum, arr)) > 0


