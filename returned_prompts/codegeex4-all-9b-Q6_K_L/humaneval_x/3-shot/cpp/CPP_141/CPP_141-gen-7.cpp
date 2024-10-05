
A few comments:

In has_close_elements, you have a potential off-by-one error.  When i=j, you'll compare a number to itself.  This won't cause a problem in your case, but it's generally a good idea to avoid it.  You can fix this by changing the inner loop to for (j=i+1;j<numbers.size();j++).

In separate_paren_groups, you're missing a check that the string ends with a closing parenthesis.  This will cause a problem if the string doesn't end with a closing parenthesis, because you'll increment level past zero, and never add the final string to all_parens.

In truncate_number, you're using the C standard library function int() to cast the number to an integer.  This is a bit unconventional, because int() is usually a macro for a function that converts a string to an integer, and in this case, it's just discarding the fractional part.  You could also use the C++ standard library function floor() to truncate the number.

In file_name_check, you're checking if the string starts with a letter with isalpha(file_name[0]), but you're not checking if the rest of the string is valid.  You should loop through the string starting with the second character, and check if each character is a letter or a digit.  You could also use the standard library function isdigit() and isalpha() to do this for you.