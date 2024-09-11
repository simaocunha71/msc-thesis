def count_occurance(string):
    count = 0
    for i in range(len(string)-2):
        if string[i:i+3] == "std":
            count += 1
    return count

# Testing the function
assert count_occurance("letstdlenstdporstd") == 3
print("All Test cases Passed")

# End of Solution




"""
Correct Solution:
To count the number of occurrence of the substring 'std' in the given string, you can use a for loop to iterate over the indices of the string from 0 to length of the string - 3. Inside the loop, check if the substring from index i to i + 3 is equal to 'std'. If it is, increment the count variable. Finally, return the count.

In the provided solution, the function count_occurance takes a string as input and initializes a count variable to 0. It then uses a for loop to iterate over the indices of the string from 0 to length of the string - 3. Inside the loop, it checks if the substring from index i to i + 3 is equal to 'std' using string slicing. If it is, it increments the count variable by 1. After the loop, it returns the count.

The assert statement is used to check if the function returns the expected result for the given test case "letstdlenstdporstd" which should be 3. If the assertion passes, it prints "All Test cases Passed", indicating that the function is working correctly.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""




"""
In the given solution, the time complexity of the function is O(n) because it iterates over the entire input string once. The space complexity is O(1) as it only uses a fixed amount of space for the count variable, regardless of the size of the input string.
"""




"""
To improve the solution, we can use regular expressions to find all occurrences of the substring 'std' in the given string. Here's an example implementation:

def count_occurance(string):
    import re
    return len(re.find