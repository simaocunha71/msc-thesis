def check_greater(arr, num):
    return all(num <= i for i in arr)  # returns False if num is greater than any element in the array