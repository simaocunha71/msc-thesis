Here is one way you can define the function:

```python
def neg_nos(nums):
    return [num for num in nums if num < 0]
```

To test this function with your example, you can use the following code:

```python
def test_neg_nos():
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    print("Pass")

test_neg_nos()
```

When you run this code, it will print "Pass" if the function is returning the expected result. 

Explanation:
The function `neg_nos` takes in a list of numbers as an argument. It uses a list comprehension to iterate over each number in the input list and checks if the number is less than zero (i.e., a negative number). If the condition is true, the number is added to a new list. Finally, the function returns the new list containing only the negative numbers.

In the provided example, the function `neg_nos` is tested with the list `[-1,4,5,-6]`. The expected output is `[-1,-6]` since these are the negative numbers in the input list. The `assert` statement is used to verify if the actual output matches the expected output. If the assertion is true, the message "Pass" is printed, indicating that the function is working correctly.

Overall, this solution provides a simple and efficient way to filter out the negative numbers from a given list using a Python function.















































































```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

