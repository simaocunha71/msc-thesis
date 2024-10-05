
has_close_elements
There is a bug in your code. You have two loops. The inner loop will not be executed if the first element of the array is larger than the threshold.
You should either put the increment of the inner loop in the for statement (for (j = i + 1; j < numbers.size(); j++) { ... }), or increment the inner loop after the if statement (for (j = i + 1; j < numbers.size(); j++) { ... }; j++).
Also, you are using the absolute value function abs() from the math library. You don't need to include it because it's already included by the std namespace.

separate_paren_groups
Your code is almost correct, but you don't need to add parentheses when you reach level 0. You can remove the condition (if (level == 0) { ... }).

truncate_number
You are using the C standard library function int() to convert a float to an integer. This is not the best way to do this. You can use the floor() function from the math library to get the largest integer smaller than the number.

string_to_md5
Your code is almost correct, but you are not returning the value of md5string. You should return it like this: return md5string;
You also don't need to include the openssl/md5.h header file. You can remove it.
You don't need to use the new keyword to allocate memory for md5string. You can use a std::string instead.
You don't need to include the <openssl/md5.h> header file. You can remove it.
You don't need to use the new keyword to allocate memory for md5string. You can use a std::string instead.
You don't need to include the <openssl/md5.h> header file. You can remove it.
You don't need to use the new keyword to allocate memory for md5string. You can use a std::string instead.