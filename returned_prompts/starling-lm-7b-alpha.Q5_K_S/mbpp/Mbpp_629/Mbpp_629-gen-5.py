def Split(List):
    res = []
    for num in List:
        if num % 2 == 0:
            res.append(num)
    return res


# Another way
def Split(List):
    return [num for num in List if num % 2 == 0]


# Test
assert Split([1,2,3,4,5]) == [2,4]


"""
Explanation:
The first function works by iterating over the list and checking if the number is divisible by 2. If it is, it appends the number to a new list. The second function uses a feature of Python called list comprehension to do the same thing in a more concise manner. In both cases, the result is a new list containing only the even numbers from the original list.
"""

"""
Explanation:
The function Split is defined to take a list of numbers as input and return a new list containing only the even numbers from the input list. The function first initializes an empty list called res to store the even numbers. Then, it iterates over each number in the input list using a for loop. Inside the loop, it checks if the current number is divisible by 2 (i.e., if it is an even number) using the modulus operator (%). If the number is even, it appends it to the res list using the append() method. Finally, it returns the res list containing all the even numbers from the input list.

The second function uses a feature of Python called list comprehension to achieve the same result in a more concise manner. Instead of using a for loop and the append() method, it creates a new list containing only the even numbers from the input list in a single line of code. The syntax [num for num in List if num % 2 == 0] means "for each number in the List, include it in the new list if it is divisible by 2". This is equivalent to the logic in the first function, but written in a more compact and Pythonic way.

To test the function, the assert statement is used to check if the function returns the expected result for a sample input. In this case, the function is expected to return [2,4] when given the input [1,2,3,4,5]. If