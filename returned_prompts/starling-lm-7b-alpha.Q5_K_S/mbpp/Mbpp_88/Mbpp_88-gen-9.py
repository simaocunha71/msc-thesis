def freq_count(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return d

# Assert
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

# Test
print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))

# Expected Output
#{10: 4, 20: 4, 40: 2, 50: 2, 30: 1}












"""
This function works by creating an empty dictionary called d. It then iterates over each number in the input list nums. For each number, it checks if the number is already a key in the dictionary d. If the number is already a key, it increments the value associated with that key by one. If the number is not already a key, it adds the number as a key in the dictionary with a value of one. Finally, it returns the populated dictionary.

The assert statement is used to verify that the function produces the expected output when given the input [10,10,10,10,20,20,20,20,40,40,50,50,30]. The expected output is the dictionary {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}. The print statement is used to test the function with the same input and verify that the expected output is produced.
"""

"""
This program defines a function called freq_count that takes a list of numbers as input and returns a dictionary containing the frequency of each number in the list. It does this by first creating