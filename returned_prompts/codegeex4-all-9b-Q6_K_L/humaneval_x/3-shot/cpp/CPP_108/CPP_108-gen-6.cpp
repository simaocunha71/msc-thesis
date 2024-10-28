
has_close_elements
Your code is mostly right but the indentation and spacing could be improved. You can also use a standard for loop instead of a goto. In general, your function is well written.
#include <cmath>
#include <vector>

bool has_close_elements(const std::vector<float> &numbers, float threshold)
{
    for (std::size_t i = 0; i < numbers.size(); i++)
        for (std::size_t j = i + 1; j < numbers.size(); j++)
            if (std::abs(numbers[i] - numbers[j]) < threshold)
                return true;

    return false;
}

separate_paren_groups
Again, your code is mostly correct but you could improve the readability. The main thing is to break up the code into smaller functions. You can also use std::accumulate instead of a manual for loop.
#include <string>
#include <vector>

std::vector<std::string> separate_paren_groups(const std::string &paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (char chr : paren_string)
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
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

truncate_number
This function is a bit tricky because of the possible precision errors. One way to fix it is to use the std::round function to round the number to the nearest integer before subtracting it.
#include <cmath>

float truncate_number(float number)
{
    return number - std::round(number);
}

count_nums
Your