
There's a lot to be said about your code, but I'll start with the basics. You've posted three functions, each of which has a main body but no function signature. This is not legal in C or C++. You need to specify the return type and the parameters of the function, like so:
bool has_close_elements(vector<float> numbers, float threshold);

vector<string> separate_paren_groups(string paren_string);

float truncate_number(float number);

int skjkasdkd(vector<int> lst);

Then, you have three functions with the same name. This is not legal in C or C++. You can't have two functions with the same name in the same scope. You need to choose different names for each function, like so:
bool has_close_elements(vector<float> numbers, float threshold);

vector<string> separate_paren_groups(string paren_string);

float truncate_number(float number);

int sum_of_digits_if_prime(vector<int> lst);

Your functions are also missing comments. Each function should have a comment describing what it does, its parameters, and its return value. For example:
/**
 * Check if any two numbers in the given vector are closer to each other than the given threshold.
 *
 * @param numbers A vector of floats.
 * @param threshold A float.
 * @return True if any two numbers in the vector are closer to each other than the threshold, false otherwise.
 */
bool has_close_elements(vector<float> numbers, float threshold);

/**
 * Separate the given string of parentheses into groups of balanced parentheses.
 *
 * @param paren_string A string containing multiple groups of nested parentheses.
 * @return A vector of strings, each containing one group of balanced parentheses.
 */
vector<string> separate_paren_groups(string paren_string);

/**
 * Return the decimal part of the given number.
 *
