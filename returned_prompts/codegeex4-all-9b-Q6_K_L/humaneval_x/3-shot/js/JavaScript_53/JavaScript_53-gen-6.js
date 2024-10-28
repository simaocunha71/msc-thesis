
Q1:
To check if there are any two numbers closer to each other than a given threshold, you can iterate through the array of numbers and for each pair of numbers, you can check the absolute difference between them and see if it's less than the threshold. If it is, return true. If you finish checking all pairs and don't find a pair that's closer than the threshold, return false.
Q2:
To separate groups of nested parentheses, you can iterate through the string and keep track of the current depth of parentheses. If you see an open parenthesis, increment the depth and add it to the current string. If you see a close parenthesis, decrement the depth, add it to the current string, and if the depth is 0, add the current string to the result array and reset the current string. Finally, return the result array.
Q3:
To truncate a number, you can use the modulus operator (%) to get the decimal part of the number. The modulus operator returns the remainder of a division operation, so when you divide the number by 1, you get the decimal part of the number.
Q4:
To add two numbers, you can simply add them together and return the result.