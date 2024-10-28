    def by_length(arr):
        arr = sorted(arr, reverse=True)
        return [str(i) for i in arr if i in range(1, 10)]

    def by_length(arr):
        arr = sorted(arr, reverse=True)
        return [str(i) for i in arr if i in range(1, 10)]

    def by_length(arr):
        arr = sorted(arr, reverse=True)
        return ['One'] if all(i not in range(1, 10) for i in arr) else [' '.join(arr[:-1]), arr[-1]]


# 3.6

