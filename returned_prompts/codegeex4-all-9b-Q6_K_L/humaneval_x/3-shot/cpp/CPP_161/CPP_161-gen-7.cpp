
has_close_elements
The algorithm is correct, but there are some room for improvements:

In the inner loop, you're using i+1, which is unnecessary. You could simply use i+1 and i+2 and increment i by 2 after each iteration. This would save you one iteration for each pair of elements.
Instead of using abs(), you could use fabs() from <cmath>. This would make your code more portable.

separate_paren_groups
Your algorithm is good, but there are some room for improvements:

You're using a for loop to iterate over the string. This is unnecessary. You could simply use a range-based for loop and use the index to access the characters.
You're using a char variable to store the current character. This is unnecessary. You could simply use the character directly in the if statements.

truncate_number
Your algorithm is correct, but there are some room for improvements:

You're using int() to convert the number to an integer. This is unnecessary. You could simply use static_cast<int>(number) or std::floor(number).
You're using a return statement inside the if block. This is unnecessary. You could simply use a return statement after the loop.

solve
Your algorithm is correct, but there are some room for improvements:

You're using a for loop to iterate over the string. This is unnecessary. You could simply use a range-based for loop and use the index to access the characters.
You're using a char variable to store the current character. This is unnecessary. You could simply use the character directly in the if statements.
Instead of using if statements to check if a character is a letter, you could use the isalpha() function from <cctype>. This would make your code more readable.