#NOTA: com 1000 tokens o output é o mesmo

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
    length_list = sorted(range(1, len(arr) + 1), reverse=True)   #Sorting the length list in reverse order.
    for number_length in length_list:
        if number_length <= len(arr):            
            if arr[number_length] >= 2 and arr[number_length] <= 9:
                str = " ".join([str(s) for s in arr[number_length].split(" ")])                   #Converting the array to string so that we can print it.
                name = list(map(str, str[::-1]))[:6]           #Taking just the first six elements of the list and removing any additional element from it.
                new_arr = [name for number_length in length_list if name == "One"]             #Creating a new array by using the name that is equal to "One" or not
