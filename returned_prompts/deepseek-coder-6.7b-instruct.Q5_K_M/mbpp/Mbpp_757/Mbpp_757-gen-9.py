def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])) # it should return 2

"""
Explanation:
The function count_reverse_pairs takes a list of strings as input. It initializes a counter to 0.
Then it goes through each string in the list with two nested loops. For each pair of strings, it checks if the string is equal to its reverse. 
If it is, it increments the counter. Finally, it returns the counter.
"""
<jupyter_output>
2
<jupyter_text>
Question 3:
<jupyter_code>
