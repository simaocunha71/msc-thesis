
has_close_elements

There's no need for a label.  Use a standard loop instead.
Use the standard library function std::abs.  It's more readable and avoids potential issues with floating point precision.
You're only using the value of j once, so there's no need for the inner loop at all.
You're returning true as soon as you find a pair of numbers that are within the threshold.  If you want to find all pairs of numbers that are within the threshold, you should collect them in a vector and return that.

separate_paren_groups

You're using the C++ string class, so there's no need to declare a C-style char array.  Just use a C++ string.
You're not handling the case where the string doesn't end with a closing brace.  In that case, you should add the current string to the vector before returning.
You don't need to check if level is zero before adding the current string to the vector.  That's already implied by the loop.

truncate_number

This is just a simple cast.  You don't need a function for this.

bf

You don't need a separate loop to find the indices of the planets in the vector.  You can use std::find.
The function should throw an exception if the input planets aren't found.  It's better to have an error condition than to return an invalid result.
You should check the order of the planets before looping.  If planet1 is after planet2, you should return an empty vector immediately.  You don't need to loop at all.
You're not returning the planets in the correct order. 