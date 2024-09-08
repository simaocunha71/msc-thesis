def get_pairs_count(lst, sum):
    count = 0
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count

print(get_pairs_count([1,1,1,1],2))

# Output: 6

# Explanation: The pairs that sum to 2 are (1, 1), (1, 1), and (1, 1). So the function returns 6.
<jupyter_output>
6
<jupyter_text>
