
You should use std::abs for absolute value, rather than the C style abs function.  Also, you should use const where possible.  Your function could be:
bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    for (std::size_t i = 0; i < numbers.size(); ++i)
    {
        for (std::size_t j = i + 1; j < numbers.size(); ++j)
        {
            if (std::abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

Note that I've used a range-based for loop to make the code a bit more readable.

In your second function, you could use a std::string constructor to create the initial string, rather than the += operator.  Also, you should use std::istringstream to split the string into tokens.  Your function could be:
std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> all_parens;
    std::istringstream iss(paren_string);
    std::string current_paren;
    char chr;

    while (iss >> chr)
    {
        if (chr == '(')
        {
            current_paren.push_back(chr);
        }
        else if (chr == ')')
        {
            current_paren.push_back(chr);
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }
    return all_parens;
}

Note that I've used the >> operator to read the next character from the stream, rather than the [] operator.  Also, I've used the clear function to clear the string, rather than the = operator.

Your third function could be:
float truncate_number(float number)
{
    return std::fmod(number, 1.0f);
}

Note that I've used the fmod function, rather than the int function.  Also, I've used 1.0f rather than 1.0 to