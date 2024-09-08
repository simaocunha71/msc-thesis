def get_Inv_Count(arr):
    """
    This function counts the number of inversions in an array.
    An inversion is a pair of elements arr[i] and arr[j] such that i < j and arr[i] > arr[j].
    """
    def merge_sort(arr, temp_arr, left, right):
        """
        This function sorts the array and counts the inversions.
        """
        inv_count = 0
        if left < right:
            mid = (left + right)//2

            inv_count += merge_sort(arr, temp_arr, left, mid)
            inv_count += merge_sort(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    def merge_and_count(arr, temp_arr, left, mid, right):
        """
        This function merges two sorted subarrays and counts the inversions.
        """
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There are mid - i inversions, because all elements left to i in the left subarray
                # are greater than arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                j += 1
            k += 1

        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into Original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    # Create a temporary array
    temp_arr = [0]*len(arr)