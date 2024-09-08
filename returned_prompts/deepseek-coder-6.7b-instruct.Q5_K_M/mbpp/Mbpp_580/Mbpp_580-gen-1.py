def extract_even(t):
    result = []
    for i in t:
        if isinstance(i, tuple):
            new_tuple = extract_even(i)
            if new_tuple:
                result.append(new_tuple)
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((4, 'a', (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((4, 'a', (7, 6, (2, 4, 'b')), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((4, 'a', (7, 6, (2, 'b', 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((4, 'a', (7, 6, (2, 'b', 4, 'c')), 6, 8)) == (4, (6, (2, 4)), 6, 8)
assert extract_even((4, 'a', (7, 6, (2, 'b', 4, 'c', 9)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3Given a list of integers, write a function to return the largest sum of non-adjacent numbers. Numbers can be 0 or negative.For example, [2, 4, 6, 2, 5] should return 13, as we pick 6 and 5. However, [5, 1, 1, 5] should return 10, as we