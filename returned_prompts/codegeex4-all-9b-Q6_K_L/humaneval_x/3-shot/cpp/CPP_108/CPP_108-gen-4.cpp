
has_close_elements:

You're checking for all pairs of numbers, but you're only returning the first pair that is closer than the threshold.  Instead, you should collect all the pairs that are closer than the threshold, and then return the number of them, or return true if there are any, or false if there are none.
You should also check that the vector has at least two elements before entering the loop.

separate_paren_groups:

This code doesn't work properly if there are no open parentheses before the closing parentheses.  For example, separate_paren_groups(")()") returns {"", "", ""}, but it should return {")", "("}.

truncate_number:

This code doesn't work properly if the input is negative.  For example, truncate_number(-3.5) returns -2.5, but it should return -0.5.

count_nums:

This code doesn't work properly if the input is negative.  For example, count_nums({-1, 11, -11}) returns 0, but it should return 1.