def next_power_of_2(n):
    if(n==0):
        return 1
    i=1
    while(i<n):
        i=i*2
    return i

def test_next_power_of_2():
    assert next_power_of_2(0) == 1
    assert next_power_of_2(1) == 2
    assert next_power_of_2(10) == 16
    assert next_power_of_2(20) == 32
    assert next_power_of_2(100) == 128
    assert next_power_of_2(1000) == 1024
    print("All tests passed.")

test_next_power_of_2()


```
  

This Python function `next_power_of_2(n)` takes a number `n` as input and returns the smallest power of 2 greater than or equal to `n`. Here's how it works:

1. It first checks if `n` is equal to 0. If so, it returns 1, as the smallest power of 2 greater than or equal to 0 is 1.
2. Then it initializes a variable `i` to 1.
3. It enters a while loop that continues until `i` is less than `n`. In each iteration of the loop, `i` is multiplied by 2. This effectively doubles the value of `i` in each iteration.
4. Once the loop ends, the function returns the final value of `i`, which is the smallest power of 2 greater than or equal to `n`.

The `test_next_power_of_2()` function is used to test the `next_power_of_2()` function with several test cases to ensure it works correctly. It asserts that the function returns the expected result for each test case. If all the assertions pass, it prints "All tests passed.".

You can use this code as a starting point and extend it to include more test cases if needed.

```python
def next_power_of_2(n):
    if(n==0):
        return