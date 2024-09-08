
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None

print(first_odd([1,3,5]))  # 1
assert first_odd([1,3,5]) == 1
<jupyter_output>
1
<jupyter_text>
Q2: Write a Python function to find the second largest number in a given list of numbers.
<jupyter_code>
