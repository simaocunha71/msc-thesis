
In your first function, you can improve efficiency by breaking out of the loop early.  You don't need to check all pairs once you've found one that fits:
bool has_close_elements(vector<float> numbers, float threshold){
    for (size_t i = 0; i < numbers.size() - 1; ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

In your second function, you can avoid the need to store the current string by just appending the character to the end of the current string.  This saves memory and is potentially faster:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
        }
        current_paren += chr;
        if (chr == ')') {
            --level;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

In your third function, you're using the C standard library function int trunc(float x) to truncate the number.  However, it's not the same as what you're doing, because trunc removes the fractional part, but rounds towards zero.  You're effectively just doing number - int(number), which is easier to write and read, but less efficient:
float truncate_number(float number) {
    return number - int(number);
}

In your fourth function, you can use std::fill to initialize the vector with the default value, and then use std::iota to fill in the values.  This is potentially faster than using a for loop:
vector<int>