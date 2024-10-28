```
def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]
```
This function uses a list comprehension to create a new list that includes only the odd numbers from the input list. The condition `num % 2 != 0` is used to check if a number is odd. The function takes a list as input and returns a new list with only the odd numbers. 

The unit test `assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]` ensures that the function is working correctly by checking if the output of the function is equal to the expected output. If the function is working correctly, the test will pass. If the function is not working correctly, the test will fail. 

This function can be used to filter odd numbers from a list. For example, if you have a list of numbers and you want to get only the odd numbers, you can use this function. 

Here's an example of how you can use this function:
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_oddnumbers(numbers)
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
```  Python 3.0
Python 2.7.15
Python 3.6.8
Python 3.7.4
Python 3.8.5
Python 3.9.5
Python 3.10.4
Python 3.11.0
Python 3.12.0
Python 3.13.0
Python 3.14.0
Python 3.15.0
Python 3.16.0
Python 3.17.0
Python 3.18.0
Python 3.19.0
Python 3.20.0
Python 3.21.0
Python 3.22.0
Python 3.23.0
Python 3.24.0
Python 3.25.0
Python 3.26.0
Python 3.27.0
Python 3.28.0
Python 3.29.0