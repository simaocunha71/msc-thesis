def max_aggregate(lst):
    dic = {}
    for name, val in lst:
        if name in dic:
            dic[name] += val
        else:
            dic[name] = val
    max_val = max(dic.values())
    max_name = [k for k, v in dic.items() if v == max_val]
    return (max_name[0], max_val)


print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))

# Output: ('Juan Whelan', 212)

# Explanation:
# Juan Whelan has the maximum aggregate value by adding up all their scores.
<jupyter_output>
('Juan Whelan', 212)
<jupyter_text>
Question 4
<jupyter_code>
