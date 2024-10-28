
has_close_elements
Your code is almost correct, but you don't need the label A: at the top. Labels are only used in GOTO statements, which are strongly discouraged. You also don't need the outer for loop, because you can use std::prev() to get the previous element in the range. You should also use auto where possible. Here's how I would write it:
bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    for (auto first = std::begin(numbers), last = std::prev(std::end(numbers)); first != last; ++first)
    {
        if (std::abs(*first - *std::next(first)) < threshold)
        {
            return true;
        }
    }
    return false;
}

separate_paren_groups
Your code is mostly correct, but it has a couple of issues. First, you need to skip over any spaces in the input string. You can do this by adding a condition to the for loop:
if (chr != ' ')
{
    // ...
}

Second, you need to check that the parentheses are balanced. You can do this by keeping track of the level of nesting and returning false if it becomes negative. Here's how I would write it:
std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    char chr;

    for (std::size_t i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];
        if (chr != ' ')
        {
            if (chr == '(')
            {
                ++level;
            }
            else if (chr == ')')
            {
                --level;
                if (level < 0)
                {
                    return {};
                }
            }
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
Your code