def first_odd(nums):
    for num in nums:
        if num % 2 == 1:
            return num
    return None

print(first_odd([1,3,5])) # 1
assert first_odd([1,3,5]) == 1
assert first_odd([2,4,6]) == None
assert first_odd([2,4,6,1]) == 1
assert first_odd([4,6,8,1]) == 1
<jupyter_output>
1
<jupyter_text>
Q2. Write a Python function to find the first even number in a given list of numbers.assert first_even([1,3,5]) == Noneassert first_even([2,4,6]) == 2assert first_even([2,4,6,1]) == 2assert first_even([4,6,8,1]) == 4
<jupyter_code>
def first_even(nums):
    for num in nums:
        if num % 2 == 0:
            return num
    return None

print(first_even([1,3,5])) # None
print(first_even([2,4,6])) # 2
print(first_even([2,4,6,1])) # 2
print(first_even([4,6,8,1])) # 4

assert first_even([1,3,5]) == None
assert first_even([2,4,6]) == 2
assert first_even([2,4,6,1]) == 2
assert first_even([4,6,8,1]) == 4
<jupyter_output>
None
2
2
4
<jupyter_text>
Q3. Write a Python function to find the index of the first odd number in a given list of numbers.If there is no odd number, return -1.assert first_odd_index([1,3,5]) == 0assert first_odd_index([2,4,6]) == -1assert first_odd_index([2,4,6,1]) == 3assert first_odd_index([4,6,8,1]) == 3
<jupy