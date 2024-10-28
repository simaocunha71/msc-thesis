
1. has_close_elements
Your function has_close_elements is correct, but it can be simplified. The only thing to consider is to use auto instead of int in the loops, and to use the range-based for loop. The following is the same code as yours, but simplified:
bool has_close_elements(vector<float> numbers, float threshold){
    for (auto first : numbers) {
        for (auto second : numbers) {
            if (first != second && abs(first - second) < threshold) {
                return true;
            }
        }
    }
    return false;
}

2. separate_paren_groups
Your function separate_paren_groups is correct, but you can use std::string::find to find the next parentheses. The following is the same code as yours, but simplified:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    size_t pos = 0;
    while (pos < paren_string.length()) {
        char chr = paren_string[pos];
        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
        pos = paren_string.find_first_of("()", pos + 1);
    }
    return all_parens;
}

3. truncate_number
Your function truncate_number is correct, but you can use std::modf to split the number into the integer and fractional parts. The following is the same code as yours, but simplified:
float truncate_number(float number){
    float integer_part;
    return modf(number, &integer_part);
}

4. rescale_to_unit
Your function rescale_to_unit is correct, but you can use std::min_element and std::