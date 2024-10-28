```
def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]
```  # or return [num for num in lst if num % 2]
```
This function uses a list comprehension to create a new list that includes only the numbers from the input list that are odd (i.e., not divisible by 2). The condition `num % 2 != 0` is used to check if a number is odd. The function takes a list as input, and returns a new list with the odd numbers. 

The unit test `assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]` checks if the function works correctly by comparing its output with the expected result. 

The function can also be written using a for loop:
```
def filter_oddnumbers(lst):
    result = []
    for num in lst:
        if num % 2 != 0:
            result.append(num)
    return result
```  # or return [num for num in lst if num % 2]
```
This function iterates over the input list, checks if each number is odd, and if it is, adds it to the result list. The result list is then returned. This function has the same functionality as the list comprehension version, but is more verbose.  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  # or return [num for num in lst if num % 2]  #