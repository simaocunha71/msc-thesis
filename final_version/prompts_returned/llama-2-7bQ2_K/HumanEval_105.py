
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    
    sorted_arr = []
    if len(arr) != 0 and (arr[0] >= 0 and arr[0] <=9): # if the first item is between 0 and 9, put it in the result array
        sorted_arr.append(str(arr[0]))
    
    if not len(sorted_arr) == 0:
        for i in range(1, len(arr)): # Loop from 1 to last element in arr (inclusive), check if it is between 0 and 9 (inclusive), put it in the result array otherwise skip
            sorted_arr.append(str(arr[i]))
    else:
        return [] # If no elements are between 0 and 9, just return an empty list
    
    reverse_sorted = sorted_array[::-1]  # Reverse the array (starting from the last element