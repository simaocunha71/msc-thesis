def max_aggregate(lst):
    d = {}
    for name, score in lst:
        if name in d:
            d[name] += score
        else:
            d[name] = score
    max_score = max(d.values())
    for name in d:
        if d[name] == max_score:
            return (name, max_score)

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))

# Output: ('Juan Whelan', 212)
<jupyter_output>
('Juan Whelan', 212)
<jupyter_text>
