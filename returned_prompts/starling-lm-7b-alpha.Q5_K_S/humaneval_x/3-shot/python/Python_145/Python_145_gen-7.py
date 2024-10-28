    def sum_of_digits(num):
        return sum(int(x) for x in str(num))

    def order_num(num):
        return (sum_of_digits(num), num)

    return sorted(nums, key=order_num)



