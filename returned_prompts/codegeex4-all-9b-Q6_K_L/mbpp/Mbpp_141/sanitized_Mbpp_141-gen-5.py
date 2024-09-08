def pancake_sort(arr):
    def flip(sub_arr):
        sub_arr.reverse()

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            flip(arr[:i + 1])
            flip(arr[:i])
    return arr