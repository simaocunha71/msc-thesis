
has_close_elements

This function is a good candidate for the standard library function std::adjacent_find.  This function will search for any pair of elements in the input range that are adjacent and satisfy a binary predicate, which could be a lambda function that checks if the absolute difference is less than the threshold.
In the function, the input vector is named numbers.  This is a fairly generic name for a vector.  It would be better to name the vector something more specific, such as scores or values.

separate_paren_groups

The function name is not very descriptive.  It would be better to name it something like group_parentheses or separate_parentheses_groups.

The variable names chr, i, and level are not descriptive.  They should be named something more meaningful.  For example, chr could be named current_character, i could be named index, and level could be named nesting_level.

The variable current_paren should be named current_group or current_parentheses.

The function should not use the goto statement.  The goto statement is rarely needed and can make code harder to understand.

The function should check if the input string is empty before attempting to iterate over it.  If the input string is empty, the function should return an empty vector.

The function should return an empty vector if the input string does not contain any balanced parentheses.

truncate_number

The function name is not very descriptive.  It would be better to name it something like get_decimal or get_fractional_part.

The function should check if the input number is negative before attempting to truncate it.  If the input number is negative, the function should return the absolute value of the truncated number.

compare

The function name is not very descriptive.  It would be better to name it something like calculate_error or compare_scores.

The function should check if the input vectors are empty before attempting to iterate over them.  If the input vectors are empty, the function should return an empty vector.

The function should return an empty vector if the input vectors have different sizes.