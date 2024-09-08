
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])) # Output: 2

Explanation:
The function `count_reverse_pairs` takes a list of strings as an argument. It initializes a counter `count` to 0. The function then iterates over each string in the list with a nested loop, comparing each string to the reversed version of the other strings in the list. If it finds a match (i.e., a string equals its reverse), it increments the counter. The function finally returns the counter, which represents the number of pairs of reverse strings it found in the list.
"""

