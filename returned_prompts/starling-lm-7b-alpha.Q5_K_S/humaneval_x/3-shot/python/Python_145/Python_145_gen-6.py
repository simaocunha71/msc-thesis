    def sum_of_digits(n):
        return sum(map(int, str(n)))

    def get_points(n):
        return -sum_of_digits(n), n

    nums.sort(key=get_points)

    return nums


