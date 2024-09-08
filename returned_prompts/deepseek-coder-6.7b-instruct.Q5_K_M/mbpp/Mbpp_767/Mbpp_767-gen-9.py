def get_pairs_count(lst, sum):
    map = {}
    twice_count = 0
    for el in lst:
        if el in map:
            map[el] += 1
        else:
            map[el] = 1
    for el in lst:
        twice_count += map[sum - el]
        if sum - el == el:
            twice_count -= 1
    return int(twice_count / 2)

print(get_pairs_count([1,1,1,1],2)) #6

"""
Explanation:
The function uses a dictionary to store the elements in the list as keys and their counts as values. Then it counts the pairs whose sum is equal to 'sum'. For each element, it checks if its complement (sum - el) exists in the dictionary. If it does, it means there is a pair whose sum is equal to 'sum', so it increases the count. If the complement is the same as the current element, it means we have counted each pair twice, so it subtracts 1 from the count. Finally, it returns the count divided by 2 because each pair is counted twice.
"""

#Time complexity: O(n)
#Space complexity: O(n)
<jupyter_output>
6
<jupyter_text>
