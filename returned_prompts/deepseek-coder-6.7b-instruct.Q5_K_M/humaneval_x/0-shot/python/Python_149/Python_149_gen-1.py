
def sorted_list_sum(lst):
    # Delete the strings that have odd lengths from the list
    lst = [i for i in lst if len(i) % 2 == 0]
    # Sort the list by length and then alphabetically
    lst.sort()
    lst.sort(key=len)
    return lst

print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # ["ab", "cd"]
print(sorted_list_sum(["aa", "a", "aaa"]))  # ["aa"]
print(sorted_list_sum(["aba", "a", "baa", "bcd"]))  # ["a", "aba", "baa", "bcd"]
print(sorted_list_sum(["abcd", "dcba", "bca", "acb"]))  # ["acb", "bca", "dcba", "abcd"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # ["ab", "cd"]
<jupyter_output>
['a', 'ab', 'baa', 'cd']
['aa']
['a', 'aba', 'baa', 'cd']
['acb', 'bca', 'dcba', 'abcd']
['ab', 'cd']
<jupyter_text>
Problem 3:
<jupyter_code>
