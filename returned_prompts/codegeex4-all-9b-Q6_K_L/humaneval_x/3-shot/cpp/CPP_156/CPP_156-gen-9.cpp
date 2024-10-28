
There is an extra level of indirection in your code.  Your A: line is superfluous.  Just remove it.
Your has_close_elements function has a name that is not very descriptive.  It might be better named as has_close_floats or something similar.  It makes the code a bit more readable.
In has_close_elements, you're using abs() which is not defined in <math.h>.  You should use std::abs() instead.  Alternatively, you can use std::fabs() which is defined in <cmath>.
In separate_paren_groups, your code is not correctly handling all cases.  For example, given the string "( ) (( )) (( )( ))", your code will produce {"()", "(())", "(()())"} instead of the expected {"()", "(())", "((()))", "(()())"}.
In int_to_mini_roman,