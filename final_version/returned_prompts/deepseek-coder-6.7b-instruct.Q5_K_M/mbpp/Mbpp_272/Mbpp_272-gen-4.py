def rear_extract(lst):
    return [x[-1] for x in lst]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))

# Alternative Solution:
def rear_extract(lst):
    return list(map(lambda x: x[-1], lst))

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))

# Alternative Solution:
def rear_extract(lst):
    return [tuple[len(tuple)-1] for tuple in lst]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))
<jupyter_output>
[21, 20, 19]
[21, 20, 19]
[21, 20, 19]
<jupyter_text>
7. Write a function that takes in a list of numbers and returns a dictionary with each number as a key and its square as the value.
<jupyter_code>
