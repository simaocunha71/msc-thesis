
has_close_elements
Your function seems to be trying to find any two elements in the vector that are within threshold of each other.  However, your function is not working as intended.  The code:
for (j=i+1;j<numbers.size();j++)

will not run when i is equal to the last index of the vector.  This is because j will be set to the same value as i, and i+1 will be equal to numbers.size().
In addition, your function will return true as soon as it finds two numbers that are within threshold of each other.  It will not check the rest of the vector.  This is likely not what you want.

separate_paren_groups
Your function is not working as intended.  You are trying to find the deepest level of nesting of parentheses, but you are not using the input string correctly.  You are treating the input string as a vector of characters, and you are using a for loop to iterate through it.  However, you are not using the current character in your loop, and you are not using the current character to determine the current level of nesting.

truncate_number
Your function is not working as intended.  You are trying to truncate a floating point number by returning the decimal part of the number.  However, you are not using the input number correctly.  You are using a cast to int to truncate the number, but this will not work as intended for negative numbers.

parse_nested_parens
Your function is not working as intended.  You are trying to parse a string of nested parentheses and return the deepest level of nesting for each group.  However, you are not using the input string correctly.  You are treating the input string as a vector of characters, and you are using a for loop to iterate through it.  However, you are not