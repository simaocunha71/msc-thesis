
def check_occurences(lst):
    dic = {}
    for tup in lst:
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1
    return dic

assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (6, 3): 1}
"""
Explanation:
The function check_occurences takes a list of tuples as input.
It initializes an empty dictionary.
It then iterates over each tuple in the input list.
If the tuple is already a key in the dictionary, it increases the corresponding value by 1.
If the tuple is not a key in the dictionary, it adds it as a key with a value of 1.
Finally, it returns the dictionary.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
