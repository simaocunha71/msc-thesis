
def sorted_list_sum(lst):
    # remove strings with odd lengths
    lst = [i for i in lst if len(i) % 2 == 0]

    # sort the list by length of each word, and then alphabetically
    lst.sort(key=lambda x: (len(x), x))

    return lst


print(sorted_list_sum(["ab", "a", "aaa", "cd"]))

# Output: ['ab', 'cd']
<jupyter_output>
['ab', 'cd']
<jupyter_text>
Question 3:
<jupyter_code>
