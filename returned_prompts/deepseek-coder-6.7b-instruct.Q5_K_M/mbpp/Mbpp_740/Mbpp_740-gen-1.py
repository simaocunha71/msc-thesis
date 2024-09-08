
def tuple_to_dict(t):
    return {t[i]: t[i + 1] for i in range(0, len(t), 2)}

print(tuple_to_dict((1, 5, 7, 10, 13, 5)))

"""
Output:
{1: 5, 7: 10, 13: 5}
"""
<jupyter_output>
{1: 5, 7: 10, 13: 5}
<jupyter_text>
Q2:
<jupyter_code>
