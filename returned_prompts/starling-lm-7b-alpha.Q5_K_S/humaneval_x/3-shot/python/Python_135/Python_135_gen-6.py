    def can_arrange(arr):
        index = -1
        for i in range(len(arr)):
            if arr[i] > arr[index]:
                index = i
        return index


