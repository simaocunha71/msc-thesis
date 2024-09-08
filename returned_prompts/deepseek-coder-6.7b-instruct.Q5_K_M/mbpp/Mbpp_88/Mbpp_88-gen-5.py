def freq_count(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))

# Output: {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

# Complexity: O(n)
<jupyter_output>
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
<jupyter_text>
Problem 2
<jupyter_code>
