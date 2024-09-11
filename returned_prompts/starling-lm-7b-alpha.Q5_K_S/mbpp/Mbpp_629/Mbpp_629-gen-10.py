def Split(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst

# Testing the function
print(Split([1,2,3,4,5])) # [2,4]


















"""
In the given problem, we need to write a python function that can find the even numbers from a list of numbers. The function should return a list containing only the even numbers from the given list.

To solve this problem, we can define a function called Split that takes a list of numbers as input. Inside the function, we initialize an empty list called new_lst to store the even numbers. Then, we iterate through each number in the input list using a for loop. For each number, we use the modulo operator (%) to check if it is divisible by 2 (i.e., if it is even). If the number is even, we append it to the new_lst using the append() method.

Finally, we return the new_lst, which contains all the even numbers from the input list.

To test the function, we can call it with a sample input list [1,2,3,4,5] and print the result. The expected output is [2,4], as these are the even numbers from the input list.
"""

```python
def Split(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst

# Testing the function
print(Split([1,2,3,4,5])) # [2,4]
```

In this code, the Split function takes a list of numbers as input and initializes an empty list called new_lst. It then iterates through each number in the input list using a for loop. For each number, it checks if it is divisible by 2 using the modulo operator (%). If the number is divisible by 2 (i.e., if it is even), it appends it to the new_lst using the append() method. Finally,