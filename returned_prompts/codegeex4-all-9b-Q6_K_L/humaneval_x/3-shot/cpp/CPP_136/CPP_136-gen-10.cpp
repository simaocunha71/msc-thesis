
In general, it looks pretty good. Some minor comments:

In has_close_elements, you're using a very poor naming convention for your variables. Don't use single-letter variable names. It's not clear what numbers and threshold represent. Use descriptive names like numbers_list and threshold_value.
The same applies to the other functions. For example, in separate_paren_groups, I wouldn't expect a string to be passed into the function; I'd expect a vector of strings.
The same applies to separate_paren_groups, where the parameter is named paren_string. I'd expect a vector of strings to be passed in, not a single string.
You're not checking that the list has at least two elements in separate_paren_groups. If you pass in an empty list, you'll get an index out of range error. You should check the length of the list before attempting to access it.
The same applies to the other functions.
In separate_paren_groups, you're using a for-loop to iterate over the string. You should be using a range-based for-loop instead, like this:

for (const auto& chr : paren_string)

In largest_smallest_integers, you're not handling the case where the list has only one element. If you pass in a list with one element, you'll get an incorrect result. You should check the length of the list before attempting to access it.
In largest_smallest_integers, you're using a very poor naming convention for your variables. Don't use single-letter variable names. It's not clear what lst, max, and min represent. Use descriptive names like list_of_integers, maximum_integer, and minimum_integer.
In truncate_number, you're using a very poor naming convention for your variable. Don't use single-letter variable names. It's not clear what number represents. Use a descriptive name like number_value.
In truncate_number, you're using a very poor naming convention for your function. Don't use single-letter variable names. It's not clear what the function does. Use a descriptive name like truncate_number_value.
In truncate_number, you're using a very poor naming convention