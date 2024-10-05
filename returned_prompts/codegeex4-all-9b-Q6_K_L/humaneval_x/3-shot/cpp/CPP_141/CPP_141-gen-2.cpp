
has_close_elements() looks good to me.  It's a bit long, but it's readable, and I don't see any obvious flaws in the algorithm.  One possible improvement is to limit the number of iterations to the size of the vector divided by 2.  That will prevent unnecessary comparisons.
For the other questions, I'll just give you hints:

separate_paren_groups() is a good start.  You'll need to add error checking to make sure that all parentheses are properly closed.  You can also make this a bit more efficient by keeping track of the current level of parentheses, and only adding a new string to all_parens when level goes to 0.
truncate_number() is straightforward.  You can also use the fmod() function to get the decimal part of a floating-point number.
file_name_check() is a bit more complex.  You'll need to split the string into the name and extension, and then check each part individually.  You can also use the isalpha() function to check if a character is a letter.

Good luck!