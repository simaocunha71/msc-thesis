def find_sum(lst):
    non_repeat = set()
    repeat = set()

    for num in lst:
        if num not in non_repeat:
            non_repeat.add(num)
        else:
            repeat.add(num)

    return sum(non_repeat - repeat)

print(find_sum([1,2,3,1,1,4,5,6]))

# Output: 21

# Explanation: 1, 2, 3, 4, 5, 6 are non-repeated numbers.
# Their sum is 21.
<jupyter_output>
21
<jupyter_text>
Question 4
<jupyter_code>
