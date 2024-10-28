
has_close_elements

You have a few bugs in this function. The most obvious is that you don't initialize j. This is a common mistake, but it's easy to fix:
for (i=0;i<numbers.size();i++)
    for (j=0;j<numbers.size();j++)

However, this function will also crash if the vector is empty. It would be better to handle that case explicitly:
if (numbers.empty()) return false;

separate_paren_groups

This function is also flawed. It doesn't handle the case where the parentheses are unbalanced. If you try to call it with an unbalanced string, it will crash. You should check the level variable at the end of the loop and return false if it's not 0:
if (level != 0) return {};

truncate_number

This function is correct, but it's not very descriptive. If you can't think of a better name, you could use something like "decimal_part".

Strongest_Extension

This function has a bug. It doesn't check whether the extensions vector is empty. If it is, the loop will crash. You should add a check at the beginning of the function:
if (extensions.empty()) return class_name + ".";

Also, the function name is not very descriptive. It would be better to use a name like "strongest_extension_name".