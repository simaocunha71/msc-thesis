
For your has_close_elements, your code is close, but you're missing a return value on your false statement. I would also recommend using a for loop with a range instead of a for loop with two indices.
Here's your code with a few minor changes:

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        for (size_t j = i + 1; j < numbers.size(); ++j)
        {
            if (abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

For your separate_paren_groups, your code is close, but you're missing a check to see if the input string is empty. I would also recommend using a for loop with a range instead of a for loop with an index.
Here's your code with a few minor changes:

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;

    if (paren_string.empty())
    {
        return all_parens;
    }

    for (size_t i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];
        if (chr == '(')
        {
            level += 1;
            current_paren += chr;
        }
        if (chr == ')')
        {
            level -= 1;
            current_paren += chr;
            if (level == 0)
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

For your truncate_number, your code is correct, but you're missing a return value on your else statement.
Here's your code with a few minor changes:

float truncate_number(float number)
{
    return number - int(number);
}

For your count_nums, your code is close, but you're missing a return value on