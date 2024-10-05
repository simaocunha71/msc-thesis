
has_close_elements
The loop condition has a logical error.  It should be j <= numbers.size() instead of j < numbers.size().  The reason is that the value of j is one more than the last element in the vector.  If you want to compare every element with every other element, you need to include that last element.
Your code uses the absolute value function abs, which is not standard for C++.  It should be std::abs instead.  Note that it is also a function in the math library, so you will need to include that header file.
You are not using the parameter threshold.  If it is not needed, remove it from the function signature.
You are not using the vector of numbers.  If it is not needed, remove it from the function signature.
Your function does not check if the input vector is empty.  If you want to handle this case, you will need to add code for that.

separate_paren_groups
This function is not complete.  It does not handle the case where there are spaces in the input string.  It also does not handle the case where there are unbalanced parentheses.  If you want to handle these cases, you will need to add code for that.
The function does not check if the input string is empty.  If you want to handle this case, you will need to add code for that.
Your function does not check if the input string contains any parentheses at all.  If you want to handle this case, you will need to add code for that.
Your function does not check if the input string contains any invalid characters.  If you want to handle this case, you will need to add code for that.

truncate_number
Your function uses the int function to convert the floating point number to an integer.  This will truncate the decimal part, which is what the problem statement specifies.  However, this will also convert negative numbers to positive, which is not what the problem statement specifies. 