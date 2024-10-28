
The first function can be greatly simplified by using the STL algorithm std::adjacent_find:
#include <algorithm>

bool has_close_elements(const std::vector<float> &numbers, float threshold)
{
    return std::adjacent_find(numbers.begin(), numbers.end(), 
        [&threshold](float a, float b){ return std::abs(a - b) < threshold; }) != numbers.end();
}

The second function has a bug. It does not handle the case where the string ends with an open parenthesis without a matching close parenthesis. To fix this, you can add a check for a non-zero level after the loop.
Also, you can simplify the code by using a range-based for loop:
#include <string>
#include <vector>

std::vector<std::string> separate_paren_groups(std::string paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;

    for (auto &chr : paren_string)
    {
        if (chr == '(')
        {
            ++level;
            current_paren += chr;
        }
        else if (chr == ')')
        {
            --level;
            current_paren += chr;
            if (level == 0)
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }

    if (level !=