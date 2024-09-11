To check if a tuple contains no duplicates, you can use a loop to go through the tuple and compare each element to the rest of the elements in the tuple. If there is a duplicate found, return False. If the loop goes through all the elements without finding any duplicates, return True. Here's a step-by-step guide:

1. Define a function called `check_distinct` that takes a tuple as an argument.
2. Initialize a variable called `found_duplicate` to False. This variable will keep track of whether a duplicate has been found or not.
3. Use a for loop to iterate through each element in the tuple. For each element, use another for loop to iterate through the rest of the elements in the tuple.
4. Inside the nested loop, check if the current element is equal to any of the remaining elements. If it is, set `found_duplicate` to True and break out of both loops.
5. After the loops, check if `found_duplicate` is still False. If it is, return True, which means that no duplicates were found. Otherwise, return False.
6. Test the function with the provided example: `assert check_distinct((1, 4, 5, 6, 1, 4)) == False`. This should return True if the function is working correctly.

Here's what the code might look like in Python:

```python
def check_distinct(t):
    found_duplicate = False
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] == t[j]:
                found_duplicate = True
                break
        if found_duplicate:
            break
    return found_duplicate
```

This function will return True if the tuple has duplicates and False if it doesn't.

```python
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
```

This test will pass if the function is correctly implemented.

```python
print(check_distinct((1, 2, 3)))  # This should return True
print(check_distinct((1, 