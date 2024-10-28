
has_close_elements

The name suggests it checks if there are close elements. However, it's a bit ambiguous what close means in this context. I would change the name to has_close_elements_by_threshold or maybe something like that.
The algorithm can be simplified by using a set to check for duplicates. It is also more efficient as it doesn't require to check all pairs in the list.
bool has_close_elements_by_threshold(const std::vector<float>& numbers, float threshold) {
    std::set<float> numbers_set(numbers.begin(), numbers.end());
    for (auto it = numbers_set.begin(); it != std::prev(numbers_set.end()); ++it) {
        if (std::next(it) != numbers_set.end() && std::abs(*it - *std::next(it)) < threshold) {
            return true;
        }
    }
    return false;
}

separate_paren_groups

The code is fine, but there is a potential bug. The string current_paren will be empty if the input string is empty, i.e. contains no parentheses. This is not a bug per se, but it might be confusing for the caller of the function. I would add a check for that and return an empty vector if the input string is empty.
Also, the name of the variable chr is a bit generic. I would rename it to c or ch.
vector<string> separate_paren_groups(const string& paren_string) {
    if (paren_string.empty()) {
        return {};
    }

    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char ch;
    for (auto it = paren_string.cbegin(); it != paren_string.cend(); ++it) {
        ch = *it;
        if (ch == '(') {
            ++level;
            current_paren += ch;
        }
        else if (ch == ')') {
            --level;
            current_paren += ch;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

truncate_number

The name of the function is fine. The