def get_pairs_count(lst, _sum):
    n = len(lst)
    m = {}
    twice_count = 0

    # count occurrences of all elements
    for i in range(n):
        if lst[i] in m:
            m[lst[i]] += 1
        else:
            m[lst[i]] = 1

    # iterate through each element and increment the count (to handle cases when sum is 0)
    for i in range(n):
        if (_sum - lst[i]) in m:
            twice_count += m[_sum - lst[i]]

        # if sum is 0, then count pairs (a,a) only if a occurs more than once
        if _sum == 0:
            twice_count -= 1

    # return half of twice_count as pairs are counted twice
    return twice_count // 2

# test cases
print(get_pairs_count([1,1,1,1],2)) # 6


"""
Explanation:
The function works by first counting the occurrences of all elements in the list using a dictionary. 
Then it iterates through each element in the list and increments the count if there is a corresponding element in the dictionary that would make the sum equal to the target sum.
If the sum is 0, it only counts pairs (a,a) if a occurs more than once.
Finally, it returns half of twice_count because each pair is counted twice (once for each element in the pair).
"""
<jupyter_output>
6
<jupyter_text>
Problem 3Given a list of integers, write a function to return the count of all possible unique triplets that add up to a given sum. The function should take as input a list of numbers and the sum, and return the count of unique triplets.
<jupyter_code>
