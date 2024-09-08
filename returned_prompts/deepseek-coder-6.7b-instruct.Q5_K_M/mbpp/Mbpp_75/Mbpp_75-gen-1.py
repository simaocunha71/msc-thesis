
def find_tuples(lst, k):
    result = []
    for tup in lst:
        if all(i % k == 0 for i in tup):
            result.append(tup)
    return result

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
<jupyter_output>
[(6, 24, 12)]
<jupyter_text>
5. Write a Python program to find the common elements in three lists using Set.
<jupyter_code>
