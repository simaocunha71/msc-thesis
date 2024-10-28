
Code organization
It's good to see the functions separated by question. I would, however, suggest a different organization: each question should have a header file that only declares the function, and one implementation file that defines it. That way, you can compile just the implementation file, and it would be easier to track down problems if there were any. (And it would be more convenient for someone else to read the code.) Then in the main file, you include the header files.
Also, I would use a more descriptive name for the functions. For example, has_close_elements could be named something like has_two_numbers_within_threshold or is_threshold_violated. Also, truncate_number would be better named extract_fractional_part.
has_close_elements
The variable names i and j are not very descriptive. You might consider something like left_index and right_index or first_index and second_index.
The function name has_close_elements is not very descriptive. The name contains_elements_within_threshold would be better.
The function has an unnecessary label A at the beginning. Labels are used to provide a location for the goto statement, and they should not be used otherwise. (In fact, the goto statement is not used in the function at all.)
The function has a redundant check numbers[i] - numbers[j] < threshold. Since the numbers are floats, the subtraction might not yield a positive number. If the two numbers are not equal, then their absolute difference must be greater than the threshold.
separate_paren_groups
The variable names chr and i are not very descriptive. You might consider something like current_character and index.
The function has an unnecessary label A at the beginning.
The function has a redundant check level == 0. Since level is initialized to 0 and incremented or decremented only by 1, it can only be 0 or 1. Therefore, you could just check if level is 1.
The function has a redundant check if (chr == ')'). You can just use if (chr == ')') { ... }.
The function has a redundant check if (level == 0) { ... }. You can just use if (level == 1) { ... }.
The function has a redundant check if (level == 0