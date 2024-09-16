def shell_sort(arr):
    def insert_sort(arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
        return arr
    def get_gap(gap):
        gap = int(gap / 2)
        if gap == 0:
            gap = 1
        return gap
    def shell_sort_main(arr):
        for gap in range(len(arr) // 2, 0, -1):
            insert_sort(arr[gap:])
        return arr
    return shell_sort_main(arr)