
In general, your code looks good, but there are some points that could be improved:

Naming
Your function names are not very descriptive.  For example, has_close_elements() does not tell me what it does, or why it is being used.  It would be better if the function names were more descriptive, such as find_close_elements() or check_for_close_elements().  This would make it easier for other developers to understand what your code is doing.
For loop
In your has_close_elements() function, you are using a for loop to iterate through the vector.  However, you are not using the index variable in your loop.  This is not a problem, but it is not necessary to use the index variable.  You can use a range-based for loop instead, which is more concise and easier to read:
for (auto number : numbers) {
    if (abs(number - numbers[i]) < threshold) {
        return true;
    }
}

This will iterate through each element in the vector, and you can access the element with the variable number.
Vectors
In your separate_paren_groups() function, you are using a vector to store the groups of parentheses.  This is a good choice, as vectors are dynamic arrays and can grow and shrink as needed.  However, you are not using any of the vector's functionality.  You could use a vector to store the groups of parentheses, and then return the vector.  This would make your code more concise and easier to read.
For loop
In your separate_paren_groups() function, you are using a for loop to iterate through the string.  However, you are not using the index variable in your loop.  This is not a problem, but it is not necessary to use the index variable.  You can use a range-based for loop instead, which is more concise and easier to read:
for (auto chr : paren_string) {
    if (chr == '('