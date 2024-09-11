"""
To solve this problem, we can create a function that takes in a list and an element as parameters. We can use a for loop to iterate through the list and check if each element is equal to the given element. If at any point we find an element that is not equal to the given element, we can immediately return False, as it means that not all items in the list are equal to the given element. If the for loop completes without finding any unequal elements, we can return True, indicating that all items in the list are equal to the given element. Here's an example implementation of the function:

def check_element(lst, elem):
    for item in lst:
        if item != elem:
            return False
    return True

To test the function, we can use the assert statement to check if the function returns the expected result when given the list ["green", "orange", "black", "white"] and the element 'blue'. The assert statement will raise an AssertionError if the condition is not met, indicating that the function is not working correctly.
"""

from __future__ import print_function
import sys

def check_element(lst, elem):
    for item in lst:
        if item != elem:
            return False
    return True

assert check_element(["green", "orange", "black", "white"],'blue')==False

# This code is contributed by 29AjayKumar

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
