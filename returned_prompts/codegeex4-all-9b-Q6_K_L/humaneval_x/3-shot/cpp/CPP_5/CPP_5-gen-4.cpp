
has_close_elements
The code can be greatly simplified by using the fact that the vector is already sorted, and using the fact that the difference between any two consecutive numbers is guaranteed to be less than the threshold.
#include <vector>
#include <algorithm>

bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    return std::adjacent_find(numbers.begin(), numbers.end(), [threshold](float a, float b){ return (b - a) < threshold; }) != numbers.end();
}

separate_paren_groups
The code can be greatly simplified by using a stack to keep track of the parentheses levels, and then extracting the strings as you pop them off the stack.
#include <vector>
#include <string>
#include <stack>
#include <cctype>

std::vector<std::string> separate_paren_groups(std::string paren_string)
{
    std::vector<std::string> all_parens;
    std::stack<std::string> paren_stack;
    std::string current_paren;
    for (char chr : paren_string)
    {
        if (chr == '(')
        {
            paren_stack.push(current_paren);
            current_paren += chr;
        }
        else if (chr == ')')
        {
            current_paren += chr;
            if (paren_stack.empty())
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
            else
            {
                current_paren = paren_stack.top() + current_paren;
                paren_stack.pop();
            }
        }
        else if (!std::isspace(chr))
        {
            current_paren += chr;
        }
    }
    return all_parens;
}

truncate_number
The code can be greatly simplified by using the modulus operator to get the fractional part of the number.
#include <cmath>

float truncate_number(float number)
{
    return std::fmod(number, 1.0f);
}

intersperse
The code can be greatly simplified by using the standard library function std::insert.
#include <vector>
#include <algorithm>

std::vector<int> intersperse(std::vector<int> numbers, int delimeter)
{
    std::vector<int> all_numbers;
    std