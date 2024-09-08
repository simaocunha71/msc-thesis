
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count


print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))

# Output: 2

Explanation:
Here, we are looping through the list and for each string we are checking whether there is any string in the rest of the list that is its reverse. If we find a reverse string, we increment our counter. The function returns the total count of such pairs.
"""

