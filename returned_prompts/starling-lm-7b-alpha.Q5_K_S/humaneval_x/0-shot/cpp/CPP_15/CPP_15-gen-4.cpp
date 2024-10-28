    if(n < 0) {
        return "";
    } else if (n == 0) {
        return "0";
    } else {
        string s = string_sequence(n-1);
        return s + " " + to_string(n);
    }
}


ANSWER:
/*
Correct Solution:
In this problem we need to create a string with space-delimited numbers starting from 0 upto n. The recursive solution is quite simple.

If the value of n is less than zero, we return an empty string, as there are no numbers to add. If n is zero, we return the string "0". Otherwise, we call the function recursively with n-1 to generate the sequence of numbers from 0 to n-1. Then we add a space and the current number (n) to the beginning of the sequence. This is done by concatenating the string with a space and the string representation of n.

For example, if we call string_sequence(5), the function will return "0 1 2 3 4 5".

The recursive function will continue to call itself until it reaches the base case of n == 0, at which point it will return "0". Then the function will return the concatenated string with the number and the space, until it reaches the base case of n < 0, at which point it will return an empty string.

This is a simple and elegant solution to the problem, as it leverages the recursive nature of the problem to generate the sequence of numbers.

*/

*/

/*
In this problem, we need to create a string containing space-delimited numbers from 0 to n. We can solve this problem using recursion.

If n is less than zero, we return an empty string because there are no numbers to add. If n is zero, we return the string "0". Otherwise, we call the function recursively with n-1 to generate the sequence of numbers from 0 to n-1. Then we add a space and the current number (n) to the beginning of the sequence. This is done by concatenating the string with a space and the string representation of n.

For example, if we call string_sequence(5), the function will return "0 1