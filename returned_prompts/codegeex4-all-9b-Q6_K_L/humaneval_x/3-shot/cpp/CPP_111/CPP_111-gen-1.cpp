
You have a few issues in your code, but they're mostly syntax errors. I'll go through them one by one.

has_close_elements()
In the function, you're using the variable i and j as loop counters, but they're also being used in the for loops. This will cause a compilation error. Also, your for loops are missing the braces.
Here's the corrected code:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i = 0; i < numbers.size(); ++i)
    {
        for (int j = i + 1; j < numbers.size(); ++j)
        {
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
        }
    }
    return false;
}

separate_paren_groups()
In the function, you're using the variable i as a loop counter, but it's also being used in the for loop. This will cause a compilation error. Also, your for loop is missing the braces.
Here's the corrected code:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (int i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];
        if (chr == '(')
        {
            level++;
            current_paren += chr;
        }
        else if (chr == ')')
        {
            level--;
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

truncate_number()
In the function, you're using the variable number as a loop counter, but it's also being used in the return statement. This will cause a compilation error.
Here's the corrected code:
float truncate_number(float number)
{
    return number - (int)number;
}

histogram()
In the function, you're using the