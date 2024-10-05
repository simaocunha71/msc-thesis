    def order_by_points(nums):
        nums.sort(key = lambda x: (sum(list(map(int, list(str(x))))), x))
        return nums

    return nums


# print(order_by_points([1, 11, -1, -11, -12]))
# print(order_by_points([]))













```