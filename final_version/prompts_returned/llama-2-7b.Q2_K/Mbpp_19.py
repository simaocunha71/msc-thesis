"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
from typing import Optional

def test_duplicate(arr: list[int]):  # pylint: disable=unused-argument,useless-super-call,useless-result,unused-argument-in-if-statement
    count = 0
    for i in arr:
        if i not in count:
            count[i]=count.get(i)+1
        else:
            print("Duplicate element {} found at index {}.".format(arr[i],count[arr[i]]))
    