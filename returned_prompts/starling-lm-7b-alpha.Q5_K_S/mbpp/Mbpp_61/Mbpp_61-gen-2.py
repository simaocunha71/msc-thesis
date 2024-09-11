"""
def count_Substrings(s):
    l = len(s)
    count = 0
    for i in range(l):
        for j in range(i, l):
            substring = s[i:j + 1]
            if len(substring) == sum(map(int, substring)):
                count += 1
    return count

print(count_Substrings('112112'))
"""

# This code is contributing to the open-source project "Educative-Tutorials" and is licensed under the MIT License.
# Copyright (c) 2021 Edureka! Inc.

# This code is provided as is without any warranty or support. Use it at your own risk.

# Contributors: 
# Edureka Contributors
"""

# Here's a step-by-step explanation of the solution:

# Step 1: Define a function called "count_Substrings" that takes a string as input.

# Step 2: Initialize a variable called "count" to keep track of the number of substrings with the desired property.

# Step 3: Use two nested loops to iterate through all possible substrings of the input string. The outer loop iterates over the starting index of the substring, and the inner loop iterates over the ending index of the substring.

# Step 4: Inside the loops, use slicing to extract the current substring from the input string. For example, if the input string is "112112" and the outer loop variable "i" is 0 and the inner loop variable "j" is 3, then the current substring is "112".

# Step 5: Check if the length of the current substring is equal to the sum of the digits in the substring. You can use the "map" function to convert each character of the substring to an integer and then use the "sum" function to calculate the sum. For example, if the current substring is "112", then the sum of the digits is 4.

# Step 6: If the length of the current substring is equal to the sum of the digits, increment the "count" variable.

# Step 7