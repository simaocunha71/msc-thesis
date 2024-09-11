"""
def get_equal(tup):
    # initialize result
    result = True
    # length of first tuple
    length = len(tup[0])
    # loop through all tuples
    for i in range(1, len(tup)):
        # if length of tuple is not equal to length of first tuple
        if(len(tup[i]) != length):
            result = False
            break
    return result

# Driver code
tup = [(11, 22, 33), (44, 55, 66)]
print(get_equal(tup))"""

The time complexity of the above function is O(n) where n is the total number of tuples in the list.

A more efficient solution is as follows:

```python
def get_equal(tup):
    # Initialize result
    result = True
    
    # Find length of first tuple
    length = len(tup[0])
    
    # Loop through all tuples
    for i in range(1, len(tup)):
        # If length of tuple is not equal to length of first tuple
        if(len(tup[i]) != length):
            result = False
            break

    # If all tuples have equal length
    if(result):
        print("All tuples have equal length")
    else:
        print("All tuples do not have equal length")
```

In this solution, instead of returning the result, we directly print the result. This is because we are only interested in whether all the tuples have equal length or not. The time complexity of this function is also O(n) where n is the total number of tuples in the list.

The above solution does not require any additional space, hence, the space complexity is O(1).

You can try running the above function with the given test case `[(11, 22, 33), (44, 55, 66)]` and it will correctly print "All tuples have equal length".

You can try running the above function with test case `[(1, 2), (3, 4, 5), (6, 7, 8,