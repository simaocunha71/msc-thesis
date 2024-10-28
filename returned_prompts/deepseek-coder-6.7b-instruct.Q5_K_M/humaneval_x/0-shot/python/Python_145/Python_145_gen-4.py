
    def get_sum(num):
        return sum(map(int, str(abs(num))))

    return sorted(nums, key=lambda num: (get_sum(num), nums.index(num)))

print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))


