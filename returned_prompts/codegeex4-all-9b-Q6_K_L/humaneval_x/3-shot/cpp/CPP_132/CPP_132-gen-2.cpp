
has_close_elements
This function is fine.  It uses two nested loops, which is not the most efficient, but it works correctly.  The name is a bit long, though, so consider using has_close_numbers.  You could also consider using two pointers instead of a nested loop.  You could do this by initializing both pointers to the start of the vector, and then moving the second pointer forward until the difference between the two values is less than the threshold.  Then you could increment both pointers and repeat until you reach the end of the vector.
separate_paren_groups
This function is mostly fine, but it doesn't handle empty strings.  It also doesn't handle strings that end with an open parenthesis.  To fix this, you could add a check for an empty string at the start of the function.  Then, you could add a check at the end of the loop to see if the current_paren is not empty and level is 0.  If so, you could add it to the all_parens vector and reset the current_paren string.
truncate_number
This function is fine.  The name is a bit long, though, so consider using get_fraction.  You could also consider using modf instead of subtracting the integer part from the number.
is_nested
This function is fine.  The name is a bit long, though, so consider using has_nested_brackets.  You could also consider using a stack instead of a level variable.  You could push an open bracket onto the stack when you see one, and then pop it off when you see a close bracket.  If the stack is not empty at the end of the loop, then there was a nested bracket.