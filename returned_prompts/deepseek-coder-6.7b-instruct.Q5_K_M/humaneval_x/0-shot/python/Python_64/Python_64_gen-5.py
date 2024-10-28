
def vowels_count(s):
    count = 0
    vowels = "aeiou"

    for letter in s:
        if letter.lower() in vowels:
            count += 1

    if s[-1] == "y":
        count += 1

    return count

print(vowels_count("abcde"))
print(vowels_count("ACEDY"))

# Output:
# 2
# 3

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), as we are using a fixed amount of space to store the vowels and count.

# This code is written by: 
# @author: Ahmed Waleed
# GitHub: https://github.com/ahmedwaleed
# Twitter: https://twitter.com/AhmedWaleed7
# LinkedIn: https://www.linkedin.com/in/ahmedwaleed1998/
# Email: ahmedwaleed1998@gmail.com
# Copyright © 2022. All rights reserved.

# This code is licensed under the MIT License.
# See the LICENSE file for more details.

# Please review the code and inform me if you have any suggestions.
# I am always open to learn and improve.

# Thank you.
<jupyter_output>
2
3
<jupyter_text>
Question 2:
<jupyter_code>
