    def smallest_change(arr):
        arr = arr[::-1]
        result = 0
        for i in range(len(arr)):
            if arr[i] != arr[i+1]:
                result += 1
        return result // 2


