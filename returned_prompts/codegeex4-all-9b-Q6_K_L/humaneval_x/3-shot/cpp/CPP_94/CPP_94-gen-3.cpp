
The first function is correct, except that you should return false instead of true when you find two numbers closer than the threshold.
The second function is also correct, but you should return all_parens by reference instead of by value, to avoid copying the vector.
The third function is incorrect. You should use the floor function to get the integer part of the number, and then subtract it from the original number to get the decimal part.
The fourth function is incorrect. You should first check if the number is prime, and then calculate the sum of its digits. You can use the fact that a number is prime if it is not divisible by any number less than itself and greater than 1.