
General

Include only what you need. In your first code block, #include<math.h> is not needed.
If you're using C++11, you can use auto for the loop variables.
Avoid using namespace std; in header files. Doing so can cause name clashes between your code and the standard library.

First problem

The function name should be is_close, not has_close_elements. The name should indicate what the function does, not how it does it.
You don't need to use abs. The difference between two floats is already a float.
You don't need the label A.
The return type of has_close_elements should be bool, not int.
Your function is very inefficient. It's O(n^2), but it can be done in O(n) by keeping track of the smallest and largest numbers seen so far, and checking whether the difference between them is smaller than the threshold.

Second problem

The function name should be separate_parenthesis_groups, not separate_paren_groups.
You don't need to keep track of the current level of parentheses. You can simply keep track of the number of open parentheses.
Your function is very inefficient. It's O(n^2), but it can be done in O(n) by scanning the string from left to right and keeping track of the number of open parentheses.

Third problem

The function name should be truncate_decimal, not truncate_number.
You don't need to cast the result to float. The result of int(number) is already a float.

Fourth problem

The function name should be count_even_odd_palindromes, not even_odd_palindrome.
You don't need to convert the number to a string. You can simply compare the number with its reverse.
You don't need to count all numbers up to n. You can simply count the numbers from 1 to n/10.