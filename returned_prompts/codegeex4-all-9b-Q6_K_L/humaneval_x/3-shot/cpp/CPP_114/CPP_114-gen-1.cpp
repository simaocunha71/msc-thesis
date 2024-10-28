
This is a good start, but there are some issues that I see:

You're missing #include <algorithm>, which is needed for std::abs.
You're missing #include <limits>, which is needed for std::numeric_limits.
Your has_close_elements function is not taking advantage of the fact that you are given a vector of floats.  You should be using the appropriate floating point comparison function.  Also, you don't need to use abs, since std::abs is a template function and will work with floats.
Your separate_paren_groups function is not handling the case where there are no parentheses in the string at all.  Your current code will result in an empty string being added to the vector, which is not the desired behavior.
Your separate_paren_groups function is not handling the case where there are multiple groups of parentheses that are not separated by whitespace.  Your current code will result in an empty string being added to the vector, which is not the desired behavior.
Your separate_paren_groups function is not handling the case where there are multiple groups of parentheses that are not separated by whitespace.  Your current code will result in an empty string being added to the vector, which is not the desired behavior.
Your separate_paren_groups function is not handling the case where there are multiple groups of parentheses that are not separated by whitespace.  Your current code will result in an empty string being added to the vector, which is not the desired behavior.
Your separate_paren_groups function is not handling the case where there are multiple groups of parentheses that are not separated by whitespace.  Your current code will result in an empty string being added to the vector, which is not the desired behavior.
Your separate_paren_groups function is not handling the case where there are multiple groups of parentheses that are not separated by whitespace.  Your current code will result in an empty string being added to the vector, which is not the desired behavior.
Your separate_paren_groups function is not handling the case where there are multiple groups of parentheses that are not separated by whitespace.  Your current code will result in an empty string