
def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count

print(count_integer([1,2,'abc',1.2]))

# Output: 2
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>
