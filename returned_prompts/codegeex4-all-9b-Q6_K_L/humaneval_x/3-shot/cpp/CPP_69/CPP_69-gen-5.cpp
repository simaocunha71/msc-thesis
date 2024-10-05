
has_close_elements

You're looping over the vector twice, which is not a great idea.  You can reduce that to a single loop by using the <algorithm> library's std::adjacent_find function.  It will return an iterator to the first pair of adjacent items that satisfy the given predicate.  If it returns the end iterator, then there were no such pairs found.
You're also not using the threshold variable at all.  You should pass a function object or lambda to the adjacent_find call, which will be used to check whether the difference between the two numbers is less than the threshold.
You're also not using the vector as a parameter, you're using a raw pointer.  It's better to use a reference, or even better, to use a const reference to avoid unnecessary copying.

separate_paren_groups

You're using the C-style for loop, which is not necessary here.  The range-based for loop is more idiomatic in C++.
You're not checking whether the string starts with an open parenthesis.  You should return an empty vector if that's the case.
The variable chr is unnecessary.  You can just use paren_string[i] directly.
You're using the C-style string concatenation operator.  You should use the + operator to concatenate strings.
You're not checking whether the string ends with a close parenthesis.  You should return an empty vector if that's the case.
The variable level is unnecessary.  You can check whether the current string is balanced by checking whether it starts with an open parenthesis and ends with a close parenthesis.

truncate_number

You should use the fmod function from <cmath> to compute the fractional part of the number.  The int() cast is not guaranteed to do what you want, because it performs a truncation, not a floor.

search

You're using a nested loop to count the occurrences of each number.  This is not very efficient.  You can use a std::map to count the occurrences in a single pass over the vector.
You're using a variable named max to store the result, which is not a good idea.  It's