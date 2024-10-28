
has_close_elements
Your function name is bad. It doesn't tell me what it does. A good name would be close_elements_exist. And, you should use a range-based for loop instead of an index-based one. It's more idiomatic.
#include <cmath>
#include <vector>

bool close_elements_exist(const std::vector<float>& numbers, float threshold)
{
    for (auto i = std::begin(numbers); i != std::end(numbers); ++i)
    {
        for (auto j = std::next(i); j != std::end(numbers); ++j)
        {
            if (std::abs(*i - *j) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
Again, the function name is bad. It doesn't tell me what it does. A good name would be split_paren_groups. And, this is a good place for a range-based for loop. It's more idiomatic. And, you can use a std::istringstream to parse the string.
#include <sstream>
#include <vector>
#include <string>

std::vector<std::string> split_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> paren_groups;
    std::istringstream iss(paren_string);
    std::string group;

    while (std::getline(iss,