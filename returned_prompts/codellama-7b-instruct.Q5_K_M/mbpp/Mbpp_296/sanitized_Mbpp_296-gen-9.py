def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    else:
        mid = len(arr) // 2
        left_count = get_Inv_Count(arr[:mid])
        right_count = get_Inv_Count(arr[mid:])
        inv_count = 0
        left = 0
        right = 0
        merged = []
        while left < len(arr) and right < len(arr):
            if arr[left] <= arr[right]:
                merged.append(arr[left])
                left += 1
            else:
                merged.append(arr[right])
                inv_count += (len(arr) - right)
                right += 1
        merged += arr[left:]
        merged += arr[right:]
        arr = merged
        return left_count + right_count + inv_count