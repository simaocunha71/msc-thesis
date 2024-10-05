
The first question is easily answered with a single line of code that uses the STL's std::adjacent_find algorithm to find two adjacent elements within a vector that are within the threshold of each other.
#include <algorithm>

bool has_close_elements(const std::vector<float>& numbers, float threshold) {
    return std::adjacent_find(numbers.begin(), numbers.end(),
                               [threshold](float a, float b) { return std::abs(a - b) < threshold; }) != numbers.end();
}

The second question is not quite as easy, since the parentheses can be nested arbitrarily.  In this case, you need to use a stack to keep track of the levels of nested parentheses.  Each time you find an open parenthesis, you push its index onto the stack.  Each time you find a close parenthesis, you pop the stack and check if the difference between the current index and the index of the open parenthesis is within the threshold.  If it is, you return true.  If you reach the end of the string without finding any close parentheses that are within the threshold of any open parentheses, you return false.
#include <stack>

std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::stack<std::size_t> open_parens;
    std::string current_paren;
    for (std::size_t i = 0; i < paren_string.length(); ++i) {
        char chr = paren_string[i];
        if (chr == '(') {
            open_parens.push(i);
            current_paren += chr;
        } else if (chr == ')') {
            if (!open_parens.empty() && i - open_parens.top() < threshold) {
                return true;
            }
            open_parens.pop();
            current_paren += chr;
            if (open_parens.empty()) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

The third question is a simple mathematical operation.  You can use the std::