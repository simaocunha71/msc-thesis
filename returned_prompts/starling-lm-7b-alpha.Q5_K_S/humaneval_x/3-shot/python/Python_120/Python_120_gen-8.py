    def maximum(arr, k):
        """
        Sort the array in reverse order, then take the first k elements.
        """
        arr.sort(reverse=True)
        return arr[:k]

    return maximum


