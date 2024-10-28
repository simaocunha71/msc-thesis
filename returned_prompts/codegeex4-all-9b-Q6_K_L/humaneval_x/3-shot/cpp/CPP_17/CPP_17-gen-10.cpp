
Code organization and readability

You have three separate functions that are not related in any way. It would be better to keep them in separate files or at least separate namespaces.
Your functions are not named well. It's hard to tell what they do. You should use descriptive names like has_close_elements_in_vector, separate_parentheses_into_groups, etc.

C++ style
You are using C++ but you are mixing C and C++ code. For example, you are using printf instead of cout, and you are using scanf instead of cin. You should stick to one style.

Code duplication
You are repeating code in all of your functions. For example, in the separate_paren_groups function, you are using a for loop to iterate over the string. You should create a separate function to do this and call it from all of your functions.

Code structure
Your code structure is not very good. You are using a single function for each question and you are not using any classes or structures. You should create a class or structure to hold the data and a function to manipulate it. This will make your code more organized and easier to understand.

Error handling
Your code does not have any error handling. For example, in the separate_paren_groups function, you are not checking if the string is empty or if the parentheses are balanced. You should add error handling to make your code more robust.

Overall, your code is not very good. It's hard to read, it's not organized well, and it doesn't handle errors. You should take the time to learn C++ properly and write better code.