    def helper(array):
        if sum(array[0], array[-1]) % 2 == 0:
            array.sort(reverse=True)
        else:
            array.sort()

    helper(array)
    return array


