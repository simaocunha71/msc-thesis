
has_close_elements:

You could use a std::sort to order the numbers, and then you would only need to check the differences of adjacent numbers. This would be much more efficient than a nested loop.
Also, you should check for edge cases, such as an empty list of numbers.

separate_paren_groups:

You have a level variable, but you don't check to make sure that it is never negative (which it could be if there are unmatched closing parentheses).
Also, you're using a std::string to build the current_paren string. This is a bit inefficient, since you're using a dynamic string (which is likely implemented as a std::vector internally), and you're doing a lot of string concatenation. You should use a std::vector<char> instead, and append the characters directly to it, then convert the vector to a string when you're done.
Also, you're not checking that the string is empty at the beginning.

truncate_number:

You're using a float, which is subject to rounding error. You should use a double instead, which is more precise.
Also, you're returning a float, but you should return a double to match the input type.

vowels_count:

You're using a std::string to build the vowels string. This is a bit inefficient, since you're using a dynamic string (which is likely implemented as a std::vector internally), and you're doing a lot of string concatenation. You should use a std::vector<char> instead, and append the characters directly to it, then convert the vector to a string when you're done.
Also, you're using the std::find function to look for the current character in the vowels string. This is a bit inefficient, since it has to search through the entire string. You should use a std::vector<std::string> instead, and use the std::find_if function to look for the current character in the vector. This would be much more efficient, since it would only have to search through the vector, not the entire string.