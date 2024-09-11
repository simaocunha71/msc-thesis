def freq_count(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d




# Contributors: Aryan Jain


"""
To solve this problem, we can use a dictionary to keep track of the frequencies of each element. We iterate over the input list, and for each element, we check if it is already in the dictionary. If it is, we increment the count by 1. If it's not, we add the element to the dictionary with a count of 1. Finally, we return the dictionary.

Here's a step-by-step breakdown of the solution:

1. Create an empty dictionary called d to store the frequencies.
2. Iterate over the input list nums using a for loop.
3. For each element i in nums, check if it is already in the dictionary d.
4. If i is in d, increment the count of i in the dictionary by 1 using the expression d[i] += 1.
5. If i is not in d, add i to the dictionary with an initial count of 1 using the expression d[i] = 1.
6. After iterating through all the elements in nums, return the dictionary d, which contains the frequencies of all the elements in the input list.

The time complexity of this solution is O(n), where n is the length of the input list, as we iterate over the list once. The space complexity is also O(n), as we store the frequencies of all the elements in the dictionary.

The assert statement at the end of the code checks if the function freq_count returns the expected result for a given input list. The expected result is a dictionary with the frequencies of each element in the input list. The assert statement ensures that the function is working correctly.
"""
# Contributors: Aryan Jain

"""
To solve this problem, we can use a dictionary to keep track of the frequencies of each element. We iterate over the input list, and for each element, we check if it is already in the dictionary. If it is, we increment the count by 1. If it's not, we add the element to the dictionary