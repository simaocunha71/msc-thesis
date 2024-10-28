
I see that you've marked this as homework, and that is great! I'm going to give you some hints that will hopefully help you solve these problems, but I'm not going to give you the solutions.
First, you need to understand what each function is supposed to do. This is the first step in solving a problem. You can do this by reading the comments above each function. For example, in the first function, the comment says:

Check if in given vector of numbers, are any two numbers closer to each other than given threshold.

This means that you need to check if there are any two numbers in the vector that are closer to each other than the given threshold. To do this, you can use a loop to iterate over all pairs of numbers in the vector, and then use the abs() function to check if the difference between the two numbers is less than the threshold.
In the second function, the comment says:

Input to this function is a string containing multiple groups of nested parentheses. Your goal is to separate those group into separate strings and return the vector of those.

This means that you need to find all the groups of nested parentheses in the string, and then separate them into separate strings. To do this, you can use a loop to iterate over all the characters in the string, and then check if the current character is an open parenthesis or a close parenthesis. If it is an open parenthesis, you need to increase a counter variable that keeps track of the current level of nesting. If it is a close parenthesis, you need to decrease the counter variable. When the counter variable reaches 0, you have found a complete group of nested parentheses, and you can add it to your vector of strings.
In the third function, the comment says:

Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1).

This means that you need to find the integer part and the decimal part of the given number