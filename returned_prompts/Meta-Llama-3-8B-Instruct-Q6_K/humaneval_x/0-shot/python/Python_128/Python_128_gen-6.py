    def prod_signs(arr):
        if not arr:
            return None

        prod_sign = 1
        sum_magnitude = 0
        for num in arr:
            if num == 0:
                return 0
            sum_magnitude += abs(num)
            prod_sign *= -1 if num > 0 else 1 if num < 0 else 0

        return sum_magnitude * prod_sign
    # test
    print(prod_signs([1, 2, 2, -4]))  # -9
    print(prod_signs([0, 1]))  # 0
    print(prod_signs([]))  # None
    print(prod_signs([-1, 1, -1, 1]))  # 0
    print(prod_signs([-2, -2]))  # 4
    print(prod_signs([1, -1, 0, 1]))  # 2
    print(prod_signs([-1, 1, 1, 1]))  # 3
    print(prod_signs([1, 1, 1, 1]))  # 4
    print(prod_signs([1, -1, 1, 1]))  # 2
    print(prod_signs([1, 1, 1, -1]))  # 2
    print(prod_signs([-1, -1, -1, -1]))  # 0
    print(prod_signs([1, 1, -1, -1]))  # 2
    print(prod_signs([-1, -1, 1, 1]))  # 2
    print(prod_signs([0, 0, 0, 0]))  # 0
    print(prod_signs([1, 1, 1, 0]))  # 3
    print(prod_signs([1, 1, 0, 1]))  # 2
    print(prod_signs([1, 0, 1, 1]))  # 2
    print(prod_signs([1, 0, 0, 1]))  # 1
    print(prod_signs([0, 1, 1, 1]))  # 3
    print(prod_signs([0, 1, 1, 0]))  # 1
    print