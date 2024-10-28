
has_close_elements

This function is fine.  It looks like you're trying to use a range-based loop but you're not actually using it.  You can simplify it like this:

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (auto i = numbers.begin(); i != numbers.end(); ++i)
    {
        auto j = i + 1;
        while (j != numbers.end())
        {
            if (abs(*i - *j) < threshold)
                return true;
            ++j;
        }
    }
    return false;
}

separate_paren_groups

This function is fine.  You can use a range-based loop here, too:

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
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

This function is fine.  It looks like you're trying to use a range-based loop but you're not actually using it.  You can simplify it like this:

float truncate_number(float number)
{
    return number - floor(number);
}

odd_count

This function is fine.  You can use a range-based loop here, too:

vector<string> odd_count(vector<string> lst)
{
    vector<string> output;
    for (const auto &str : lst)
    {
        string current;
        for (char chr : str)
        {
            if (isdigit(chr))
            {
                int num = chr - '0';
                if (num % 2 == 1)
                    current += num;
            }
       