
1.  has_close_elements
    No need for A: label, it is a comment, and you should use it to describe the function.  No need to declare i,j, and level, and no need to do the computation inside the function body.  This is a good use for a range-based for loop:
bool has_close_elements(const std::vector<float>& numbers, float threshold) {
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i+1; j != numbers.end(); ++j) {
            if (std::abs(*i - *j) < threshold) {
                return true;
            }
        }
    }
    return false;
}

2.  separate_paren_groups
    No need for A: label, it is a comment, and you should use it to describe the function.  No need to declare all_parens, current_paren, level, i, and chr, and no need to do the computation inside the function body.  This is a good use for a range-based for loop:
std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (auto chr : paren_string) {
        if (chr == '(') {
            ++level;
            current_paren += chr;
        }
        if (chr == ')') {
            --level;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

3.  truncate_number
    No need for A: label, it is a comment, and you should use it to describe the function.  No need to declare number, and no need to do the computation inside the function body.  This is a good use of std::modf:
float truncate_number(float number