    def helper(array):
        first_last_sum = array[0] + array[-1]
        if first_last_sum % 2 == 1:
            array.sort()
        else:
            array.sort(reverse=True)
        return array

    return helper(array[:])


