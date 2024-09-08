def move_zero(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst

print(move_zero([1,0,2,0,3,4]))

# Alternative solution
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

# Alternative solution
def move_zero(lst):
    return sorted(lst, key=lambda x: x==0)

print(move_zero([1,0,2,0,3,4]))
<jupyter_output>
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
<jupyter_text>
**Task 3**
<jupyter_code>
