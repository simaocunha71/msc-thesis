    def get_sum(x):
        return sum(int(i) for i in str(x))

    return sorted(nums, key=lambda x: (get_sum(x), nums.index(x)))


