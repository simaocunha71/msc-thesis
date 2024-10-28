
has_close_elements
Your function's name suggests that it checks if there are elements close to each other. The current function name suggests that it checks if there are two elements close to each other, but the function checks if there are any two elements close to each other. I would rename it to has_close_elements or has_close_pairs.

In your function, you do not need the label A. It is not clear what it is for, but it is not needed.
In your function, you do not need a for loop with a single iteration. You can just return false.

separate_paren_groups
Your function's name suggests that it separates groups of parentheses. The current function name suggests that it separates groups of parentheses into separate strings. However, the function separates groups of parentheses into separate strings, but it does not check if the parentheses are balanced. I would rename it to separate_balanced_paren_groups or separate_balanced_paren_groups_into_strings.

In your function, you do not need the variable i. You can just use a range-based for loop.
In your function, you do not need the variable chr. You can just use paren_string[i].
In your function, you do not need the variable level. You can just use a counter.
In your function, you do not need the variable current_paren. You can just use a stringstream.

truncate_number
Your function's name suggests that it truncates a number. The current function name suggests that it truncates a number to the integer part. However, the function truncates a number to the decimal part. I would rename it to truncate_decimal.

In your function, you do not need the cast to int. You can just use int(number).

anti_shuffle
Your function's name suggests that it anti-shuffles a string. The current function name suggests that it anti-shuffles a string into an ordered version of it. However, the function anti-shuffles a string into an ordered version of it, but it does not keep the order of words and blank spaces in the sentence. I would