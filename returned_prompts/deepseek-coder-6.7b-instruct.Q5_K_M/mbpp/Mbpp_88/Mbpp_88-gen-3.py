def freq_count(lst):
    freqs = {}
    for i in lst:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
    return freqs

print(freq_iq([10,10,10,10,20,20,20,20,40,40,50,50,30]))

# Output: {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

# Explanation: The function works by iterating through the list and checking if each element is already in the dictionary.
# If it is, it increments the count by 1. If it's not, it adds the element to the dictionary with a count of 1.
# Finally, it returns the dictionary.


# Alternative solution using dictionary comprehension and count function
def freq_count(lst):
    return {i: lst.count(i) for i in lst}

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))

# Output: {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

# Explanation: This solution works by creating a dictionary where each key is a unique element from the list and each value is the count of that element in the list.
# The count function is used to count the number of times each element appears in the list.
# This solution will work, but it's less efficient for large lists because the count function needs to be called for each element in the list.
# The first solution is more efficient because it only needs to iterate through the list once.
<jupyter_output>
{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
{10: 