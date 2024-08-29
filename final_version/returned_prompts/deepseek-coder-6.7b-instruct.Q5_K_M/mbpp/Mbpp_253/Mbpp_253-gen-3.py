def count_integer(lst):
    return len([i for i in lst if isinstance(i, int)])

print(count_integer([1,2,'abc',1.2]))

# or

def count_integer(lst):
    return sum(isinstance(i, int) for i in lst)

print(count_integer([1,2,'abc',1.2]))

# or

def count_integer(lst):
    return sum(map(lambda x: isinstance(x, int), lst))

print(count_integer([1,2,'abc',1.2]))

# or

def count_integer(lst):
    return sum(filter(lambda x: isinstance(x, int), lst))

print(count_integer([1,2,'abc',1.2]))
<jupyter_output>
2
2
2
2
<jupyter_text>
Problem 2
<jupyter_code>
