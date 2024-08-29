def find_sum(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    non_repeated = [num for num, count in counts.items() if count == 1]
    return sum(non_repeated)

print(find_sum([1,2,3,1,1,4,5,6]))

"""
This solution works by first counting the frequency of each number in the list. Then, it creates a list of the numbers that only appear once. Finally, it returns the sum of these numbers.
"""

"""
What is the time complexity of this solution?
"""

A: The time complexity of this solution is O(n), where n is the length of the list. This is because it goes through the list once to count the numbers and then again to create the list of non-repeated numbers.
"""
What is the space complexity of this solution?
"""

A: The space complexity of this solution is O(n), where n is the length of the list. This is because it uses a dictionary to count the numbers in the list, which can potentially have as many entries as there are numbers in the list if all are different.
"""
What is the complexity of the function "sum" in Python?
"""

A: The complexity of the function "sum" in Python is O(n), where n is the length of the list. This is because it goes through the list once to sum the numbers.
"""
So, the total time complexity of this solution is O(n) + O(n) + O(n) = O(n). Is that correct?
"""

A: Yes, that's correct. The time complexity of the function is O(n) because it performs a constant amount of work for each element in the list.
"""
Does this solution work for negative numbers as well?
"""

A: Yes, this solution works for negative numbers as well. The counts dictionary will correctly handle negative numbers as keys, and they will be correctly counted as non-repeated or repeated.

"""
Can you modify the function to find the sum of non-repeated elements in a given list where the list can have negative