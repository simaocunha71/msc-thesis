def max_occurrences(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = max(count.values())
    for key in count:
        if count[key] == max_count:
            return key

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))

# OUTPUT: 2
<jupyter_output>
2
<jupyter_text>
**Question 2**
<jupyter_code>
