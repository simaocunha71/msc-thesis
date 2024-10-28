
Here are some comments on your code:

You should use std::abs instead of abs in has_close_elements. The former is part of the C++ standard library and the latter is a macro in the C standard library. It's better to use the C++ standard library when possible.
You have used using namespace std;. This is fine, but you should be aware of what it does. It adds all of the names in the std namespace to your file. If two libraries both have a function or class with the same name, this can cause problems. For example, if you were to include <numeric>, it has a function named add. If you included both <numeric> and your own add function, you would have a conflict. To avoid this, you should use the namespace prefix when you can.
Your add function returns an int. It's more flexible to return a float or double, since it can handle larger numbers.
In separate_paren_groups, you don't check whether the parentheses are balanced. For example, if the input is "(", your code will fail.
In separate_paren_groups, you don't check for invalid characters. If the input contains anything other than parentheses, your code will fail.
In separate_paren_groups, you don't check for multiple groups of parentheses in a row. For example, if the input is "((()))", your code will return {"((()))"}, not {"()", "()", "()"}. This could be fixed by adding a check to see if the current character is a parenthesis, and if so, whether the next character is a parenthesis or the end of the string.
In truncate_number, you could use floorf to truncate the number, instead of subtracting the integer part. This would be more accurate, especially for very large numbers.
In add, you could use the += operator to add the two numbers, instead of using the + operator. This is more flexible, since it can handle larger numbers.
In add, you could use the auto keyword to let the compiler deduce the return type. This would make the function more flexible, since it could handle any type of numbers.