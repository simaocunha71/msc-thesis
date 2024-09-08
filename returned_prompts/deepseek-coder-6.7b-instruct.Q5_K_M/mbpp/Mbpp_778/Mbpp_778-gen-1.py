
def pack_consecutive_duplicates(lst):
    result = []
    i = 0
    while i < len(lst):
        start = i
        while i < len(lst)-1 and lst[i] == lst[i+1]:
            i += 1
        result.append(lst[start:i+1])
        i += 1
    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])) #[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
Explanation:
The function goes through the list and whenever it sees consecutive duplicates, it packs them into a sublist.
"""
<jupyter_output>
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
<jupyter_text>
Q2. Write a Python function that takes a list of strings and returns a new list with all strings converted to lowercase.
<jupyter_code>
def to_lowercase(lst):
    return [s.lower() for s in lst]

print(to_lowercase(["Hello", "WORLD"]))  # ['hello', 'world']
<jupyter_output>
['hello', 'world']
<jupyter_text>
Q3. Write a Python function that takes a list of integers and returns the sum of all the even integers in the list.
<jupyter_code>
def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

print(sum_even_numbers([1, 2, 3, 4, 5, 6])) 