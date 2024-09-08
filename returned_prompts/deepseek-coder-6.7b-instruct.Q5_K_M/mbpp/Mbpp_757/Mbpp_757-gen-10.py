def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])) # 2


"""
Explanation:
The function count_reverse_pairs takes a list of strings as input. It initializes a count variable to 0. 
It then uses two nested loops to go through each string in the list. 
For each pair of strings, it checks if the second string is the reverse of the first string (by comparing it with the reverse of the first string). 
If it is, it increments the count. At the end of the function, it returns the count.
"""
<jupyter_output>
2
<jupyter_text>
