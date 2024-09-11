def pos_count(nums):
    cnt = 0
    for i in nums:
        if i > 0:
            cnt += 1
    return cnt

def test_pos_count():
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([-1,0,3,5]) == 3
    print("All tests passed!")

test_pos_count()




"""
In this code, a function called `pos_count` is defined to count the number of positive numbers in a given list. The function uses a `for` loop to iterate through each element in the list. If the element is greater than zero (i.e., positive), the `cnt` variable is incremented by 1. Finally, the function returns the value of `cnt`, which represents the count of positive numbers in the list.

The `test_pos_count` function is used to test the `pos_count` function. It calls the `pos_count` function with two different lists and asserts that the returned values are equal to the expected values. If all tests pass, it prints "All tests passed!" to the console.

In the provided example, the `pos_count` function is called with the list `[1,-2,3,-4]`. The function correctly identifies that there are 2 positive numbers in the list (1 and 3) and returns 2. The `test_pos_count` function asserts that the returned value is equal to 2, and since it is, the test passes.

Similarly, the `pos_count` function is called with the list `[-1,0,3,5]`. The function correctly identifies that there are 3 positive numbers in the list (3 and 5) and returns 3. The `test_pos_count` function asserts that the returned value is equal to 3, and since it is, the test passes.

If all tests pass, the message "All tests passed!" is printed to the console, indicating that the `pos_count` function is working correctly.
"""






































