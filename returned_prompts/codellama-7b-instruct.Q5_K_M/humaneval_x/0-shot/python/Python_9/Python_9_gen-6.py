    def rolling_max(numbers):
        return list(max(numbers[i:] for i in range(len(numbers))))
