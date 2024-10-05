
Your functions are all correct, but I'll go through each one and suggest some improvements.

has_close_elements

The code is good, but it's not using C++ idioms. The range-based for loop, and the auto keyword, can be used to make it more idiomatic.
Also, you should be using the std::abs function instead of the abs macro, which is not guaranteed to work on float types.

Code:
bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    for (const auto& num : numbers)
    {
        for (const auto& other : numbers)
        {
            if (num != other && std::abs(num - other) < threshold)
            {
                return true;
            }
        }
    }

    return false;
}

separate_paren_groups

The code is good, but you should be using std::string::find and std::string::substr to find the first opening parenthesis and then extract the substring up to the matching closing parenthesis.
Also, you should be using std::string::empty to check if the current_paren string is empty, and std::string::length to get its length.

Code:
std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    std::size_t pos;

    while ((pos = paren_string.find_first_of("()")) != std::string::npos)
    {
        if (paren_string[pos] == '(')
        {
            ++level;
            current_paren += paren_string[pos];
        }
        else
        {
            --level;
            current_paren += paren_string[pos];

            if (level == 0)
            {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }

        paren_string.erase(0, pos + 1);
    }

    return all_parens;
}

truncate_number

The code is good, but you should be using the std::