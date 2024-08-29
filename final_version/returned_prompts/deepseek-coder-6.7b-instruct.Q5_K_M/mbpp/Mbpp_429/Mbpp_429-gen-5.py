def not_tuples(t1):
    return tuple(~x for x in t1)

print(not_tuples((10, 4, 6, 9)))
<jupyter_output>
(15, 6, 5, 8)
(-5, -1, -7, -10)
<jup