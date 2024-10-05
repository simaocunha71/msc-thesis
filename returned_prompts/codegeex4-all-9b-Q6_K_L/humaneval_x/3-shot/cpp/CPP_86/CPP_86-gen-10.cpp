
I don't like your A: comments at the start of each function. They're not useful and they're ugly.
Comments should explain why something is done rather than what is done. Comments should be used to explain what is not obvious from the code. The code itself should be self-explanatory where possible.
Your comments should start with a capital letter and end with a full stop.
Your function names are good (though your naming style is inconsistent, some are camelCase and some are all lower case with underscores). Your variable names are good too, though the variable names are a bit long and repetitive. You might consider shortening them.

has_close_elements
The name has_close_elements is not very descriptive. It's not clear what it means by "close".
It's not clear what you mean by "closer than". Do you mean closer than the threshold or closer than half the threshold? It's not clear how close is close enough. Is the threshold the maximum difference or is it the minimum difference? 

You should have comments explaining all the parameters, especially the threshold.
You should also have comments explaining the return value.

You should also have comments explaining the algorithm.

separate_paren_groups
This function is not very clear. It's not clear what the function does or what it returns.
The parameter name paren_string is not very descriptive. It's not clear what it represents.
The function name separate_paren_groups is not very descriptive. It's not clear what it separates or groups.

You should have comments explaining all the parameters, especially the paren_string parameter.
You should also have comments explaining the return value.

You should also have comments explaining the algorithm.

truncate_number
The function name truncate_number is not very descriptive. It's not clear what it truncates or what it returns.
The parameter name number is not very descriptive. It's not clear what it represents.

You should have comments explaining all the parameters, especially the number parameter.
You should also have comments explaining the return value.

You should also have comments explaining the algorithm.

anti_shuffle
The function name anti_shuffle is not very descriptive. It