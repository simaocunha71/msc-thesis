```
def filter_oddnumbers(numbers):
    return [num for num in numbers if num % 2 != 0]
```
The function takes a list of numbers as input and returns a new list containing only the odd numbers from the input list. The list comprehension iterates over each number in the input list and checks if the number is odd by using the modulus operator (%). If the remainder is not zero (i.e., the number is odd), it is included in the output list. The resulting list of odd numbers is returned by the function.