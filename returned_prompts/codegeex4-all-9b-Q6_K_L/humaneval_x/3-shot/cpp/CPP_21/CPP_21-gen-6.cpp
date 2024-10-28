
has_close_elements
The for loops are too nested. You can just use a single loop and compare each number in turn to the others. The complexity of your function is O(n^2). It can be reduced to O(n) by using an std::set which stores the numbers in sorted order.
#include <set>

bool has_close_elements(const std::vector<float>& numbers, float threshold) {
    std::set<float> sorted_numbers(numbers.begin(), numbers.end());
    auto i = sorted_numbers.begin(), j = std::next(i);
    while (j != sorted_numbers.end()) {
        if (*j - *i <= threshold) {
            return true;
        }
        ++i;
        ++j;
    }
    return false;
}

separate_paren_groups
The algorithm is mostly correct, but it doesn't handle the case where the input string is empty. Also, it doesn't handle the case where there is an odd number of parentheses.
Here is a modified version of your code that handles these cases.
#include <vector>
#include <string>

std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            if (level == 0) {
                current_paren.clear();
            }
            ++level;
        } else if (chr == ')') {
            if (level == 0) {
                throw std::runtime_error("Unmatched closing parenthesis");
            }
            --level;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    if (level != 0) {
        throw std::runtime_error("Unmatched opening parenthesis");
    }
    return all_parens;
}

truncate_number
Your