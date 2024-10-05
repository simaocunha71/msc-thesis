
1. has_close_elements

This function is not correct. For example, has_close_elements({1.0, 2.0, 3.0, 4.0, 5.0, 2.0}, 0.3) should return true, because 2.0 and 2.0 are closer than 0.3, but it returns false.
The problem is in the loop, you compare every pair of numbers in the vector. It should be enough to compare every number with the next one.
Also, you don't need to use abs function, because you are comparing with a positive number.

2. separate_paren_groups

This function is not correct. For example, separate_paren_groups("( ) (( )) (( )( ))") should return {"()", "(())", "(()())"}, but it returns {"()", "(())"}.
The problem is in the loop, you don't check if the current character is a closing parenthesis. You should check it and add the current_paren to all_parens only if it is a closing parenthesis.

3. truncate_number

This function is not correct. For example, truncate_number(3.5) should return 0.5, but it returns 3.0.
The problem is in the cast to int, you are casting