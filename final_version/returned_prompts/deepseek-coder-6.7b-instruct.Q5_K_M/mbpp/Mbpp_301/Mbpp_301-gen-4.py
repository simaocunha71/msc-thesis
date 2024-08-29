
def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))
<jupyter_output>
4
<jupyter_text>
Problem 4:
<jupyter_code>
