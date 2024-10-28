    def sum_digits(n):
        return sum(map(int, str(n)))

    def order(a,b):
        return sum_digits(a) - sum_digits(b), a-b

    return sorted(nums, key = lambda x: order(x,nums[order(nums[0],x)[1]]))


