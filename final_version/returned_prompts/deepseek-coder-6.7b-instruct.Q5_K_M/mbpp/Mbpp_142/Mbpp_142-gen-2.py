
def count_samepair(l1, l2, l3):
    return sum(a == b == c for a, b, c in zip(l1, l2, l3))

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))

"""
Here, we use the built-in zip function to combine the three lists into a single sequence of tuples. We then use a generator expression to generate 1s for each position where the corresponding elements of the tuples are all the same and 0s otherwise. The sum function then adds up these 1s to give the count of positions where the corresponding elements are the same.
"""
<jupyter_output>
3
<jupyter_text>
Question 7
<jupyter_code>
