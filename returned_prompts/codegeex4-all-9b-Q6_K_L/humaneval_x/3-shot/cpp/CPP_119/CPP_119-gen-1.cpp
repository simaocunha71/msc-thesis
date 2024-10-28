
has_close_elements
The name has_close_elements is not very descriptive.  It's not immediately clear what is meant by "close" elements, or what is considered "close".  Perhaps has_elements_within_threshold would be more descriptive?
Also, the loop is structured inefficiently.  It's better to loop over the range [i, j) rather than [i, j] so that you don't need to check the boundary conditions.
Also, your function is not exception-safe.  It does not check if the vector is empty, and it does not check if the vector contains only one element.  This could lead to undefined behavior.
Here's the improved code:
bool has_elements_within_threshold(const vector<float>& numbers, float threshold) {
    if (numbers.size() < 2) {
        throw std::invalid_argument("vector must contain at least two elements");
    }

    for (size_t i = 0; i < numbers.size() - 1; ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (std::abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }

    return false;
}

separate_paren_groups
The function separate_paren_groups has a bug.  It does not properly handle the case where there is a space between the parentheses.  For example, separate_paren_groups("( ) (( )) (( )( ))") returns {"()", "(", ")", "((", " ", ")", "(", ")", ")", "(", ")", ")", "}", "(( )( ))"} instead of {"()", "(())", "(()())"}.
Here's the improved code:
vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;

   