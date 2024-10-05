
The first question is easily answered with the STL algorithm std::adjacent_find
#include <algorithm>
bool has_close_elements(std::vector<float> const& numbers, float threshold)
{
    return std::adjacent_find(numbers.begin(), numbers.end(),
        [threshold](float a, float b)
        {
            return std::abs(a - b) < threshold;
        }) != numbers.end();
}

The second question is a bit more complex, and requires some parsing. I've written a function to do this, but you'll need to write the actual code to add and remove parentheses from the string:
#include <string>
#include <vector>

std::vector<std::string> separate_paren_groups(std::string const& paren_string)
{
    std::vector<std::string> result;
    std::string current;
    bool in_group = false;
    for (char c : paren_string)
    {
        if (c == ' ')
            continue;

        if (c == '(')
        {
            if (in_group)
                current += c;
            else
            {
                in_group = true;
                current += c;
            }
        }
        else if (c == ')')
        {
            if (in_group)
            {
                current += c;
                if (!add_group(result, current))
                    return {};
                in_group = false;
                current.clear();
            }
            else
                return {};
        }
        else
        {
            if (in_group)
                current += c;
            else
                return {};
        }
    }
    if (in_group)
        return {};
    return result;
}

bool add_group(std::vector<std::string>& groups, std::string& group)
{
    // check if group is balanced
    int level = 0;
    for (char c : group)
    {
        if (c == '(')
            ++level;
        else if (c == ')')
        {
            if (--level < 0)
                return false;
        }
    }
    if (level != 0)
        return false;

    groups.push_back