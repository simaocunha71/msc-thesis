    arr = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    def by_length(arr):
        arr = sorted(arr, key=lambda x: len(x))
        arr.reverse()
        res = []
        for num in arr:
            if 1 <= int(num) <= 9:
                res.append(arr[int(num)-1])
            else:
                res.append(num)
        return res
    # by_length([2, 1, 1, 4, 5, 8, 2, 3])
    # print(by_length([1, -1 , 55]))
    # print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
    # print(by_length([]))
    # print(by_length([1, 'two', 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    return by_length(arr)



```