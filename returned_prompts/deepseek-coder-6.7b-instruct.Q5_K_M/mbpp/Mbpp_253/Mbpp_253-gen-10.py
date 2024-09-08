def count_integer(lst):
    return sum(1 for i in lst if isinstance(i, int))

# test
assert count_integer([1,2,'abc',1.2]) == 2

# Alternative solution
def count_integer(lst):
    return len([i for i in lst if isinstance(i, int)])

# test
assert count_integer([1,2,'abc',1.2]) == 2

# Alternative solution
def count_integer(lst):
    count = 0
    for i in lst:
        if isinstance(i, int):
            count += 1
    return count

# test
assert count_integer([1,2,'abc',1.2]) == 2
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python function that returns the number of even integers in a given list.assert count_even([1,2,'abc',1.2]) == 1
<jupyter_code>
def count_even(lst):
    return len([i for i in lst if isinstance(i, int) and i % 2 == 0])

# test
assert count_even([1,2,'abc',1.2]) == 1
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python function that returns the number of odd integers in a given list.assert count_odd([1,2,'abc',1.2]) == 1
<jupyter_code>
def count_odd(lst):
    return len([i for i in lst if isinstance(i, int) and i % 2 != 0])

# test
assert count_odd([1,2,'abc',1.2]) == 1
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a Python function to return the sum of all numbers in a list.assert sum_all([1,2,'abc',1.2]) == 4.2
<jupyter_code>
def sum_all(lst):
    return