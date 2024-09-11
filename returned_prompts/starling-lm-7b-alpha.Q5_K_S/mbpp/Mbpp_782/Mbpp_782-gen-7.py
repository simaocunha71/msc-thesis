def odd_length_sum(arr):
    return sum(i+1 for i in range(len(arr)))

def test_odd_length_sum():
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,3,4,5,6]) == 30
    assert odd_length_sum([1,2,3,4]) == 18
    print("All Test Cases Passed")

test_odd_length_sum()


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Explanation: 

To find the sum of all odd length subarrays, we can simply sum all the indices of the given array. This is because, for an array of length n, there are (n+1) odd length subarrays, and each subarray is represented by its starting index to ending index. 

For example, given an array [1,2,4], there are three odd length subarrays: [1], [1,2], [1,2,4]. The sum of the indices of these subarrays is 1+2+3 = 6.

The function odd_length_sum(arr) calculates the sum of all indices of the given array using a list comprehension and the range function. The range function generates a sequence of numbers from 0 to n-1, where n is the length of the array. We add 1 to each index to account for the starting index of the subarray. The sum function then adds up all the indices.

The function test_odd_length_sum() tests the odd_length_sum function with a few sample inputs to verify its correctness. If all the test cases pass, it prints "All Test Cases Passed".

The time complexity of the odd_length_sum function is O(n) because we need to iterate through all the indices of the array. The space complexity is O(1) because we don't use any extra data structures that depend on the input size.

"""







```

```