
There are some issues with your code, but I'll point out the major ones:

You are missing #include <algorithm> at the top of your file. This is required for the use of the abs() function.
The code for has_close_elements() is missing a closing brace. This means the compiler will not be able to compile your code.
Your code for separate_paren_groups() is missing a closing brace, similar to the above issue.
Your code for truncate_number() is missing a closing brace.
Your code for skjkasdkd() is missing a closing brace.
Your code for skjkasdkd() is missing a return statement. You need to return the sum variable.
Your code for skjkasdkd() is not checking if the largest number in the list is prime. You need to add a function to check if a number is prime.
Your code for skjkasdkd() is not adding the digit sum of the largest prime number to the sum variable. You need to add this code.
Your code for skjkasdkd() is not handling the case where there are no prime numbers in the list. You need to add a check for this case and return 0 if no prime numbers are found.