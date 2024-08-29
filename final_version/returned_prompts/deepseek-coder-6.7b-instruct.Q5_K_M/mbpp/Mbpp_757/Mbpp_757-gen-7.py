
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))  # 2


"""
In this solution, we iterate over the list and for every string we iterate over the rest of the list. 
If the string equals its reverse (achieved by lst[i][::-1]), we increment our counter.
"""


# Time complexity: O(n^2 * m), where n is the number of strings in the list and m is the length of the strings.
# This is because we have two nested loops, each running up to n times and for each of these iterations we perform a string comparison which takes up to m operations.

# Space complexity: O(1), we only use a fixed amount of space to store the count variable and the indices i and j, so the memory usage does not grow with the size of the input.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
