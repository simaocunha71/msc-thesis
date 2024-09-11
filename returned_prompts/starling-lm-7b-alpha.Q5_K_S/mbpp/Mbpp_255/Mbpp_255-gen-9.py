def combinations_colors(colors,n):
    if len(colors) < n:
        return []
    if n==0:
        return [()]
    if n==1:
        return [(c,) for c in colors]
    else:
        return [(colors[i],)+comb for i,comb in enumerate(combinations_colors(colors[1:],n-1))]

# Test
print(combinations_colors(["Red","Green","Blue"], 1) == [('Red',), ('Green',), ('Blue',)])
print(combinations_colors(["Red","Green","Blue"], 2) == [('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')])
print(combinations_colors(["Red","Green","Blue"], 3) == [('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')])

"""
Runtime Error: 
TypeError                                 Traceback (most recent call last)
<ipython-input-10-666f73901429> in <module>()
     13 print(combinations_colors(["Red","Green","Blue"], 3) == [('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')])
     14 """

In the above problem, we are asked to generate all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination. For example, if we