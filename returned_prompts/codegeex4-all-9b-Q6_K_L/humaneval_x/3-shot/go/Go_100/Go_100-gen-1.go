
Q1: Check if in given list of numbers, are any two numbers closer to each other than given threshold.
A1: You can solve this by iterating over the array of numbers and comparing each number with every other number. If the absolute difference between two numbers is less than the threshold, return true. If no such pair is found, return false.

Q2: Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those group into separate strings and return the list of those.
A2: You can solve this by iterating over the string and maintaining a count of open and close parentheses. Whenever the count of open parentheses is zero, it means a group of parentheses is completed. Add the group to the result list and reset the count. Continue this until the end of the string.

Q3: Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number.
A3: You can solve this by subtracting the integer part of the number from the number itself. The integer part can be obtained using the math.Floor function.

Q4: Given a positive integer n, you have to make a pile of n levels of stones. The first level has n stones. The number of stones in the next level is: - the next odd number if n is odd. - the next even number if n is even. Return the number of stones in each level in a list, where element at index i represents the number of stones in the level (i+1).
A4: You can solve this by initializing an array of length n and filling it with the number of stones in each level. The number of stones in each level can be calculated using a loop and the formulas given in the problem statement.