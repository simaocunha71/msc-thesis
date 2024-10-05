
Code for 1st question:

You can use std::adjacent_find for this question. But since it's not allowed to use STL, we can write our own function to check if there are two elements in a vector that are closer than a certain threshold. One way to do it is to use two nested for loops to iterate over the vector and check the absolute difference between each pair of elements. If the absolute difference is less than the threshold, return true. If the loop completes without finding any such pair, return false.

Code for 2nd question:

The given code seems to be correct. It iterates over the string and adds each character to the current_paren string until it reaches a closing parenthesis. Then it checks if the level is 0, which means that the current group of parentheses is complete and can be added to the all_parens vector. Finally, it returns the all_parens vector.

Code for 3rd question:

The given code seems to be correct. It simply subtracts the integer part of the number from the number itself to get the decimal part.

Code for 4th question:

The given code seems to be correct. It iterates over the numbers from 0 to n-1 and checks if each number is divisible by 11 or 13. If it is, it converts the number to a string, iterates over the digits and checks if any of them is 7. If it is, it increments the count variable. Finally, it returns the count variable.