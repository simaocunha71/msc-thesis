    def add_elements(arr, k):
        sum = 0
        for i in range(k):
            if len(str(arr[i])) <= 2:
                sum += arr[i]
        return sum

    return add_elements(arr, k)


