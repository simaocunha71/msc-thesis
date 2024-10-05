    def get_sum(num):
        return sum(map(int, str(num)))

    return sorted(nums, key=lambda x: (get_sum(x), x))


