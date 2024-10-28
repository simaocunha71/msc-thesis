    def helper(array, ascending=True):
        if len(array) == 0:
            return []

        return sorted(array, reverse=not ascending)

    return helper(array, sum(array[0], array[-1]) % 2 == 0)


