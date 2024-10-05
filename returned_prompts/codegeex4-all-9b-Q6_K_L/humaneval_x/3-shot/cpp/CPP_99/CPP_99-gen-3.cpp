
1. has_close_elements

You're using a goto here, which is not good practice. Also, you don't need two loops here. You can simply go through the vector once and compare each number to the next one.
The comparison part can be simplified using the following line:
if (abs(numbers[i] - numbers[j]) < threshold) return true;

Also, it's better to use the auto keyword when declaring a variable that's the result of a function call:
for (auto i = 0; i < numbers.size(); ++i)
{
    for (auto j = i + 1; j < numbers.size(); ++j)
    {
        if (abs(numbers[i] - numbers[j]) < threshold) return true;
    }
}

2. separate_paren_groups

Your code is not checking for balanced parentheses. You should use a stack to check if each open parenthesis is properly closed, and if not, you should ignore the rest of the string.
Also, you're not handling the case where there's no closing parenthesis for an opening parenthesis. For example, if the input is "((", your code will return an empty string instead of the correct answer, which is "(". Similarly, if the input is "(()", your code will return "()" instead of "()".
Here's a more robust implementation:
#include <stack>
#include <sstream>
#include <stdexcept>

std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> all_parens;
    std::stack<char> paren_stack;
    std::stringstream current_paren;
    char chr;

    for (std::size_t i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];

        if (chr == '(')
        {
            paren_stack.push(chr);
            current_paren << chr;
        }
        else if (chr == ')')
        {
            if (paren_stack.empty())
            {
                throw std::runtime_error("Unbalanced parentheses");
            }

            paren_stack.pop();
            current_paren << chr;

            if (paren_stack.empty())
            {
                all_parens.push_back(current_paren.str());
                current_paren.str("");
            }
        }
        else if (!std::isspace(chr))
        {
            throw std::runtime_error("Invalid character");
        }
    }

    if