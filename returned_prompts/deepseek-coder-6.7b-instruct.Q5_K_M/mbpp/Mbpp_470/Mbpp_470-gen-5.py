def add_pairwise(t):
    return tuple(a+b for a, b in zip(t[:-1], t[1:]))

print(add_pairwise((1, 5, 7, 8, 10)))

# 6, 12, 15, 18
<jupyter_output>
(6, 12, 15, 18)
<jupyter_text>
