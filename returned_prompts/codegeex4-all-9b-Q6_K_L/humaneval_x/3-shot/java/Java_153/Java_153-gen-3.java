
Q1: Given a list of numbers, check if any two numbers are closer to each other than a given threshold.
A: Iterate through the list and calculate the absolute difference between each pair of numbers. If the difference is less than the threshold, return true. If no such pair is found, return false.
Q2: Given a string containing multiple groups of nested parentheses, separate the groups into separate strings and return the list of those.
A: Iterate through the string and keep track of the current depth of parentheses. When a closing parenthesis is encountered, check if the depth is 0. If it is, add the current group to the result list and reset the current group. Return the result list at the end.
Q3: Given a positive floating point number, truncate the number to its decimal part.
A: Return the remainder of the number when divided by 1.0.
Q4: Given a class name and a list of extensions, find the strongest extension and return a string in the format: ClassName.StrongestExtensionName.
A: Iterate through the list of extensions and calculate their strength using the given formula. Keep track of the extension with the highest strength. Return a string in the format: ClassName.StrongestExtensionName.