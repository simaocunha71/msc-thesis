    # First, create a dictionary which maps each element to its index
    # Then iterate over the dictionary to find the largest index whose key is less than its preceding key
    # If such an index is not found, return -1
    def can_arrange(arr):
        idx_dict = {}
        for i, v in enumerate(arr):
            idx_dict[v] = i
        for i in range(len(arr) - 1, 0, -1):
            if idx_dict[arr[i]] > idx_dict[arr[i-1]]:
                return idx_dict[arr[i]]
        return -1

