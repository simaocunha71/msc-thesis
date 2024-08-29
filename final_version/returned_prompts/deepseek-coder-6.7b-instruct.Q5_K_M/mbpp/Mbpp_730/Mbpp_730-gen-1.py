
def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))

#Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
<jupyter_output>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
<jupyter_text>
Question 2:
<jupyter_code>
