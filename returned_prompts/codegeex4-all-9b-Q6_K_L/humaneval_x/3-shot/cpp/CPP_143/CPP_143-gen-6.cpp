
First, I want to tell you, your code works. However, I have some comments regarding your code style.
1. Use meaningful variable names, for example, for the first question, use vector instead of numbers.
2. Use the standard library to check if a number is prime. You can use isprime function in <algorithm> for this purpose.
3. For the second question, you don't need to use a string to store the current parentheses. You can use a integer to represent the level, which can simplify your code.
4. For the third question, there is a standard library function fmod to get the decimal part of a number.
5. For the fourth question, you can use a for loop to iterate over the sentence and check if the length of each word is prime. If it is, append it to the result.