def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    else:
        mid = len(arr) // 2
        left_count = get_Inv_Count(arr[:mid])
        right_count = get_Inv_Count(arr[mid:])
        inv_count = 0
        i = 0
        j = 0
        k = 0
        while i < mid and j < len(arr) - mid:
            if arr[i] <= arr[j]:
                i += 1
            else:
                j += 1
                inv_count += mid - i
        return left_count + right_count + inv_count
