
First, I'll comment on each of the functions, and then I'll give some general advice.

has_close_elements

You're not using the vector and float parameters, and you're not handling the case where the vector is empty.  You also have a label A:, which doesn't seem to be doing anything.
Here's a cleaned-up version:
bool has_close_elements(const vector<float>& numbers, float threshold) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (std::abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Note that I've used size_t for the loop counters, because it's the natural type for sizes and counts.  I've also changed the parameters to be const references, to avoid copying the vectors, and to allow the function to be used with temporary vectors.
separate_paren_groups

You're not handling the case where the string is empty, and you're not handling the case where the parentheses are unbalanced.  Also, you're using a char when a char* or const char* would be more appropriate.
Here's a cleaned-up version:
vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (size_t i = 0; i < paren_string.length(); ++i) {
        char chr = paren_string[i];
        if (chr == '(') {
            ++level;
            current_paren += chr;
        } else if (chr == ')') {
            --level;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens