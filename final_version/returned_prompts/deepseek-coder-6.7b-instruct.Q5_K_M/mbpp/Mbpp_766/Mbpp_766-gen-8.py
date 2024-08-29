def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

print(pair_wise([1,1,2,3,3,4,4,5]))
<jupyter_output>
[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
<jupyter_text>
Question 2
<jupyter_code>
