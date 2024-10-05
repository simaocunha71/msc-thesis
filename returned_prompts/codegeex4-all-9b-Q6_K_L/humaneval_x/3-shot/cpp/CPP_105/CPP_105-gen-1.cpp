
The first question is straightforward. You have to iterate over all pairs of numbers and compare the absolute difference to the threshold.
Your implementation is good, but you can make it more efficient by breaking out of the inner loop when you find two numbers that are close enough.
#include <vector>
#include <cmath>
#include <algorithm>

bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        for (size_t j = i + 1; j < numbers.size(); ++j)
        {
            if (std::abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

For the second question, you are asked to split a string into groups of balanced parentheses. You can do this by iterating over the string and keeping track of the current level of nesting. When you encounter an opening parenthesis, you increase the level and add the parenthesis to the current group. When you encounter a closing parenthesis, you decrease the level and add the parenthesis to the current group. If the level becomes zero, you have finished a group and can add it to the list of groups.
Your implementation is close, but it has a bug. When you encounter a closing parenthesis, you add it to the current group before checking if the level is zero. This means that the closing parenthesis will be part of the next group instead of the current one.
#include <vector>
#include <string>
#include <sstream>

std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> groups;
    std::string current_group;
    int level =