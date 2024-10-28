    def sum_of_digits(x):
        result = 0
        while x != 0:
            result += x % 10
            x = x // 10
        return result

    def count_nums_helper(arr):
        count = 0
        for elem in arr:
            if sum_of_digits(elem) > 0:
                count += 1
        return count

    return count_nums_helper(arr)


