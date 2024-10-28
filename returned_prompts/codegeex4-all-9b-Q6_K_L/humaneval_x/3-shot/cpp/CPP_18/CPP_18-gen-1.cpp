
First, I'll say that I'm not a fan of the way you've structured your code. You have a function which calls itself, and your for loops are nested. This is not a good idea.
The function has_close_elements:
This function is supposed to return a boolean value, but your code does not return anything in case of a match, which is undefined behavior. You should change the function signature to:
bool has_close_elements(vector<float> numbers, float threshold);

And then return false at the end of the function if no match is found.
The function separate_paren_groups:
This function is supposed to return a vector of strings, but your code does not return anything in case of an error, which is undefined behavior. You should return an empty vector at the end of the function if no match is found.
The function truncate_number:
This function is supposed to return a float value, but your code does not return anything in case of an error, which is undefined behavior. You should return 0.0 at the end of the function if the input number is not a positive floating point number.
The function how_many_times:
This function is supposed to return an int value, but your code does not return anything in case of an error, which is undefined behavior. You should return 0 at the end of the function if the input string is empty.