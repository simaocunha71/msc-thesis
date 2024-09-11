def is_Monotonic(array):
    return (all(array[i] <= array[i+1] for i in range(len(array)-1)) or 
            all(array[i] >= array[i+1] for i in range(len(array)-1)))  # check if array is either non-decreasing or non-increasing
    # or 
    # return array == sorted(array) or array == sorted(array, reverse=True)  # check if array is either non-decreasing or non-increasing
    # return array == sorted(array, reverse=True)  # check if array is non-increasing
    # return array == sorted(array)  # check if array is non-decreasing
    # return all(array[i] <= array[i+1] for i in range(len(array)-1)) or all(array[i] >= array[i+1] for i in range(len(array)-1))  # check if array is either non-decreasing or non-increasing
    # return all(array[i] <= array[i+1] for i in range(len(array)-1))  # check if array is non-decreasing
    # return all(array[i] >= array[i+1] for i in range(len(array)-1))  # check if array is non-increasing
    # return array == sorted(array, reverse=True) or array == sorted(array)  # check if array is either non-increasing or non-decreasing
    # return array == sorted(array) or array == sorted(array, reverse=True)  # check if array is either non-decreasing or non-increasing
    # return array == sorted(array)  # check if array is non-decreasing
    # return array == sorted(array, reverse=True)  # check if array is non-increasing
    # return all(array[i] <= array[i+1] for i in range(len(array)-1))  # check if array is non-decreasing
    # return all(array[i] >= array[i+1] for i in range(len(array)-1))  # check if array is non-increasing
    # return array == sorted(array)  # check if array is non-decreasing
    # return array == sorted(array, reverse=True)  # check if array is non-increasing
    # return array == sorted(array)  # check if array is non-decreasing
    # return array == sorted(array, reverse=True)  # check if array is non-increasing
    # return array