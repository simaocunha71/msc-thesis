
has_close_elements has no return value. You should return true or false after the loop.
Your inner loop should be from i+1 to numbers.size() - 1 (not i+2).
Also, you don't need to use abs() for float. You can use the - operator directly.

separate_paren_groups has a bug. If there is a closing parenthesis without an opening one, the function will enter the if statement and try to access an element outside of the vector. You should check if level is equal to 0 before accessing all_parens.

truncate_number doesn't do anything with the input number. You should return the result of number - int(number).

bf has a bug. You are using the variable k, which is not declared. You should use a different variable name for the second index. Also, you should return an empty vector if planet1 or planet2 are not in the planets vector.