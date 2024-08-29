def remove_odd(lst):
    return [n for n in lst if n % 2 == 0]

print(remove_odd([1,2,3]))

# or

def remove_odd(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

print(remove_odd([1,2,3]))

# or

def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]

print(remove_odd([1,2,3]))

# or

def remove_odd(lst):
    return [n for n in lst if n % 2 == 0]

print(remove_odd([1,2,3]))
<jupyter_output>
[2]
[2]
[2]
[2]
<jupyter_text>
