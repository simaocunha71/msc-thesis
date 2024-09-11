```
def frequency(a, b):
    return a.count(b)
```

Explanation:
In the above solution, we are using the built-in count method of the list data type in Python. This method counts the number of occurrences of a particular element in the list and returns the count. We can use this method to count the occurrences of a number in the given list.

The function frequency takes two arguments - a (the list) and b (the number we want to count the occurrences of). Inside the function, we use the count method of the list a to count the occurrences of the number b and return the count.

For example, if we call the function frequency([1,2,3], 4), it will return 0 because the number 4 does not occur in the list [1,2,3].

This solution is simple and straightforward, but it might not be the most efficient for large lists as the count method has a time complexity of O(n), where n is the length of the list.

If you are working with large lists and performance is a concern, you might want to consider using a more efficient approach, such as using a dictionary to count the occurrences of each element in the list.
```
def frequency(a, b):
    count = 0
    for elem in a:
        if elem == b:
            count += 1
    return count
```

In this alternative solution, we initialize a variable count to 0. Then, we iterate over each element in the list a. If the current element is equal to the number b, we increment the count by 1. Finally, we return the count, which represents the number of occurrences of the number b in the list a.

This solution has a time complexity of O(n), where n is the length of the list, similar to the previous solution. However, it does not use the built-in count method and might be more efficient for large lists.
```


# Assertion Code:
def test_frequency():
    assert frequency([1,2,3], 4) == 0
    print("All tests passed.")


test_frequency()
```

In the above assertion code, we define a function test_frequency that