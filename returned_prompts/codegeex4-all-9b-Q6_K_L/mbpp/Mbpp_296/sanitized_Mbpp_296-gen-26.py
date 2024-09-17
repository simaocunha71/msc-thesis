def get_Inv_Count(nums):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_nums = merge_sort(nums)
    inversions = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if sorted_nums.index(nums[i]) > sorted_nums.index(nums[j]):
                inversions += 1
    return inversions