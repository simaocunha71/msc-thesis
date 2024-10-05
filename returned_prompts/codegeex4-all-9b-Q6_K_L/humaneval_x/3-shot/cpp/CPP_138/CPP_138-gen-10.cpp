
There is nothing to review yet, since you have not posted the questions.  However, here are a few general tips:

Make sure you comment your code.  It's not clear from your sample code what the purpose of each function is, or what the parameters are.  At the very least, you should have comments at the top of each function explaining what the function does, and what parameters are expected and what they represent.
Use consistent indentation.  The indentation in the sample code is inconsistent.  You should use consistent indentation to make your code easier to read and understand.
Avoid using the "using namespace std;" directive.  This can lead to name conflicts, and it's generally better to use the std:: prefix when using standard library types and functions.
Make sure you return the correct type from each function.  In the sample code, the functions are returning bool, but the comments indicate that they should be returning float and vector<string> instead.  You should fix the return types to match the comments.
Use braces {} for all if statements, even if they only have one statement.  This makes your code easier to read and understand.
Make sure you check for integer division when you are using division with integers.  In the sample code, the function truncate_number is using integer division, which will truncate the decimal part of the number.  If you want to keep the decimal part, you should use floating point division instead.
Make sure you handle all possible input values.  In the sample code, the function is_equal_to_sum_even does not handle the case where n is less than 8.  You should add a check for this case and return false if n is less than 8.
Make sure you handle all possible edge cases.  In the sample code, the function separate_paren_groups does not handle the case where the input string is empty.  You should add a check for this case and return an empty vector if the input string is empty.
Make sure you handle all possible error cases.  In the