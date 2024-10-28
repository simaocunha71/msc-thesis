
You are on the right track.  Here are some suggestions:

The function names should be more descriptive.  For example, has_close_elements is better than A.
In has_close_elements, the inner loop's index should be j, not i.  (You don't want to compare each pair of numbers twice.)
In separate_paren_groups, I would suggest using a stringstream to build the current_paren string.  This will make it easier to handle cases where the parentheses are not balanced (e.g., "((").
In separate_paren_groups, you should check that level is positive before adding current_paren to all_parens.  (It will be negative if there are more closing parentheses than opening ones.)
In separate_paren_groups, you should check that paren_string[i] is a parenthesis before adding it to current_paren.
In truncate_number, you should check that number is greater than 0.  (Otherwise, int(number) will be the same as number, and the return value will be 0.)
In encode_shift and decode_shift, you should check that s[i] is a lowercase letter before adding it to out.  (Otherwise, the result will be undefined behavior.)