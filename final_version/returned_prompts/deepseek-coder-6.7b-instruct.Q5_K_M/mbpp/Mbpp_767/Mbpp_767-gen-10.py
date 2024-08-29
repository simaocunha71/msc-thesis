def get_pairs_count(arr, sum):
    map = {}
    twice_count = 0
    for i in range(0, len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    for i in range(0, len(arr)):
        twice_count += map[sum - arr[i]]
        if (sum - arr[i]) == arr[i]:
            twice_count -= 1
    return int(twice_count / 2)

print(get_pairs_count([1,1,1,1],2)) #6

"""
Explanation:
The function works by first counting the number of times each number appears in the input list, then it counts the number of times the sum of two numbers is equal to the target sum. It subtracts one from this count for each pair where one number is equal to the half of the target sum, because each such pair is counted twice. The result is divided by 2 to correct for the double-counting.
"""
<jupyter_output>
6
<jupyter_text>
Question 2:Given two strings, write a python function to calculate the Levenshtein Distance between them. The function should return the number of changes required to change one string into the other.
<jupyter_code>
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s