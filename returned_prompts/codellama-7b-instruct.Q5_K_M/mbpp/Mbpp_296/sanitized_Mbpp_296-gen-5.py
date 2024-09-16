def get_Inv_Count(arr):
    def merge_count(arr, l, m, r):
        count = 0
        left = arr[l:m]
        right = arr[m:r]
        left_idx = 0
        right_idx = 0
        output = []
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                output.append(left[left_idx])
                left_idx += 1
            else:
                output.append(right[right_idx])
                right_idx += 1
                count += len(left) - left_idx
        output.extend(left[left_idx:])
        output.extend(right[right_idx:])
        arr[l:r] = output
        return count
    def merge_sort_count(arr, l, r):
        if l < r:
            m = (l + r) // 2
            count = merge_sort_count(arr, l, m)
            count += merge_sort_count(arr, m, r)
            count += merge_count(arr, l, m, r)
        return count
    return merge_sort_count(arr, 0, len(arr))