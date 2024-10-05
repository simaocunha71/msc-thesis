
Your first function has_close_elements has the following issues:

Your loop is not checking all pairs of elements.  The condition j = i + 1 means that you are only checking adjacent elements, not all pairs.
You do not need the label A: inside the function.  This is not a good practice and can lead to confusion.
You don't need to use abs() to calculate the absolute difference.  The subtraction of two floats already gives you the absolute difference.

Here's a corrected version of your first function:
bool has_close_elements(vector<float> numbers, float threshold) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (fabs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Your second function separate_paren_groups has the following issues:

You are not handling the case where the input string does not contain any parentheses.  This will cause an infinite loop.
You are not handling the case where the input string contains unmatched parentheses.  This will cause an infinite loop.
You are not handling the case where the input string contains nested parentheses.  This will cause incorrect results.
You are not handling the case where the input string contains spaces.  This will cause incorrect results.
You are not handling the case where the input string contains multiple groups of parentheses.  This will cause incorrect results.

Here's a corrected version of your second function:
vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr