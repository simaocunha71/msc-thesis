
def sorted_list_sum(lst):
    lst = [i for i in lst if len(i) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))

print(sorted_list_sum(["ab", "a", "aaa", "cd"]))
print(sorted_list_sum(["aa", "a", "aaa"]))
<jupyter_output>
['ab', 'cd']
['aa']
<jupyter_text>
Question 3
<jupyter_code>
