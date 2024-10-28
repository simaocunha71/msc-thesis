
has_close_elements
Your loop is fine, but you're not using a function to check the difference.  Instead, just use subtraction:
if (numbers[i] - numbers[j] < threshold)
    return true;

separate_paren_groups
You're not checking if you've reached the end of the string, but you're still trying to access the characters.  This is undefined behavior, and will likely cause your program to crash.
You should add a check for the end of the string, and if you've reached the end, return the current string.

truncate_number
You're not using a function to convert the integer part to a float.  Use static_cast<float> or double:
return number - static_cast<float>(int(number));