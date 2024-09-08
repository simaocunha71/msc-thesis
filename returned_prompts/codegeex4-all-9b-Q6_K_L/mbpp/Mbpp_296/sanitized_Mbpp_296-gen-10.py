def get_Inv_Count(array):
    """
    Count the number of inversions in an array.

    :param array: List[int] - The input array
    :return: int - The number of inversions
    """
    def merge_sort(arr):
        """
        Merge sort helper function.

        :param arr: List[int] - The input array
        :return: List[int], int - The sorted array and the number of inversions
        """
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        merged, merge_inv = merge(left, right)
        return merged, left_inv + right_inv + merge_inv

    def merge(left, right):
        """
        Merge two sorted arrays and count the number of inversions.

        :param left: List[int] - The left sorted array
        :param right: List[int] - The right sorted array
        :return: List[int], int - The merged array and the number of inversions
        """
        merged = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv += len(left) - i
        merged += left[i:]
        merged += right[j:]
        return merged, inv

    _, inversions = merge_sort(array)
    return inversions