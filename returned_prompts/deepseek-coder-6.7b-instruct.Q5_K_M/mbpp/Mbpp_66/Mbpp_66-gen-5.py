def pos_count(lst):
    count = 0
    for i in lst:
        if i > 0:
            count += 1
    return count

print(pos_count([1,-2,3,-4]))

# Alternative solution using List comprehension
def pos_count(lst):
    return len([i for i in lst if i > 0])

print(pos_count([1,-2,3,-4]))

# Alternative solution using sum function
def pos_count(lst):
    return sum(i > 0 for i in lst)

print(pos_count([1,-2,3,-4]))
<jupyter_output>
2
2
2
<jupyter_text>
Question 2
<jupyter_code>
