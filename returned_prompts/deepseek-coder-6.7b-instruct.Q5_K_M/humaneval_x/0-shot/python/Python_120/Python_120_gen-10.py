
    # Solution 1
    # Sorting
    # Time complexity: O(n log n)
    # Space complexity: O(n)

    arr.sort(reverse=True)
    return arr[:k]

    # Solution 2
    # Heap
    # Time complexity: O(n log k)
    # Space complexity: O(k)

    import heapq
    return heapq.nlargest(k, arr)

    # Solution 3
    # Quick select
    # Time complexity: O(n) in the average case, O(n^2) in the worst case
    # Space complexity: O(1)

    def partition(l, h):
        pivot = arr[h]
        i = l
        for j in range(l, h):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[h] = arr[h], arr[i]
        return i

    def quickselect(l, h, k):
        if l == h:
            return arr[l]
        pivot_index = partition(l, h)
        if pivot_index == k:
            return arr[k]
        elif pivot_index > k:
            return quickselect(l, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, h, k)

    return [quickselect(0, len(arr) - 1, i) for i in range(k)]

    # Solution 4
    # Bucket sort
    # Time complexity: O(n + k)
    # Space complexity: O(n + k)

    min_val, max_val = min(arr), max(arr)
    size = max_val - min_val + 1
    bucket = [0] * size
    count = [0] * size
    for num in arr:
        bucket[num - min_val] += 1
    for i in range(1, size):
        count[i] = count[i - 