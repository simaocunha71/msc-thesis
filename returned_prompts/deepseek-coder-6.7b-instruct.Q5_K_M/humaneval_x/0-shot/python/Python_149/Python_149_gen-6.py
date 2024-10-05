
def sorted_list_sum(lst):
    even_length_list = [x for x in lst if len(x) % 2 == 0]
    even_length_list.sort()
    return even_length_list

print(sorted_list_sum(["ab", "a", "aaa", "cd"]))
print(sorted_list_sum(["aa", "a", "aaa"]))
<jupyter_output>
['ab', 'cd']
['aa']
<jupyter_text>
Q2: Write a Python function to find the largest and smallest numbers in a list.
<jupyter_code>
