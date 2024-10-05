
The first function has_close_elements has a minor issue: the second loop should start at i+1. Otherwise, you will compare each number with itself which is not meaningful.
Here's the corrected version:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i = 0; i < numbers.size(); i++)
        for (int j = i + 1; j < numbers.size(); j++)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

The second function separate_paren_groups has another minor issue: you are trying to add a character to a string that might not be a parenthesis. You should add the character only if it is an opening or closing parenthesis. Otherwise, you should ignore it. Also, your code does not handle the case when the input string has no parentheses. In this case, the function should return an empty vector. Here's the corrected version:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); i++)
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
                current_paren = "";
            }
        }
    }
    return all_parens;
}

The third function truncate_number is correct. It uses