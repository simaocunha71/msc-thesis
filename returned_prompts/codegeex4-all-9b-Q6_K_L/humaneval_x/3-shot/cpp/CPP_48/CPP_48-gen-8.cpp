
You've got three functions that are almost identical, and very easy to understand.
You could make this easier on yourself by creating a template function for your first two functions. That way you could avoid duplicating code. You could use a template parameter to indicate the type of the number. Something like this:
template <typename T>
bool has_close_elements(vector<T> numbers, T threshold) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

You could also consider using the standard library algorithms to make this easier and more efficient. For example:
template <typename T>
bool has_close_elements(vector<T> numbers, T threshold) {
    return adjacent_find(numbers.begin(), numbers.end(), [&](T lhs, T rhs) {
        return abs(lhs - rhs) < threshold;
    }) != numbers.end();
}

In your second function, you could use the std::istringstream to parse the input string. It would make it easier to read the input and handle errors.
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::istringstream iss(paren_string);
    std::string current_paren;

    for (char c; iss >> c;) {
        if (c == '(') {
            ++current_paren;
        } else if (c == ')') {
            ++current_paren;
            if (current_paren.size() == 2) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }

    return all_parens;
}

I'm not sure what you're trying to accomplish with the truncate_number function. The math library provides a function that does this already. You can use the modf function to get the fractional part of a number. Here's an example of how you could use it:
float truncate_number(float number) {
    float integer_part;
    float fractional_part =