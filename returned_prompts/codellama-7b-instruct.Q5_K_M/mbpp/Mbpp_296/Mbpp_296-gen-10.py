def get_Inv_Count(arr):
    def merge_and_count(left, right):
        inv_count = 0
        left_idx = 0
        right_idx = 0
        merged = []
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
                inv_count += len(left) - left_idx
        merged += left[left_idx:]
        merged += right[right_idx:]
        return merged, inv_count
    def merge_sort_and_count(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left, inv_count_left = merge_sort_and_count(arr[:mid])
            right, inv_count_right = merge_sort_and_count(arr[mid:])
            merged, inv_count = merge_and_count(left, right)
            return merged, inv_count_left + inv_count_right + inv_count
        return arr, 0
    merged, inv_count = merge_sort_and_count(arr)
    return inv_count
