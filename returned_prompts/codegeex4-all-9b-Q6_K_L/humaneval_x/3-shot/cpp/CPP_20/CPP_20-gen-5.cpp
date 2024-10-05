
Your has_close_elements function is not correct.  It is missing the declaration of the variables i, j and the return statement.  Here is the corrected version:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i = 0; i < numbers.size(); ++i)
        for (int j = i + 1; j < numbers.size(); ++j)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

Your separate_paren_groups function is mostly correct, but you don't need the level variable.  Here is the corrected version:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    for (char chr : paren_string)
    {
        if (chr == '(')
            current_paren += chr;
        else if (chr == ')')
        {
            current_paren += chr;
            if (current_paren.length() == 2)
            {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

Your truncate_number function is correct.

Your find_closest_elements function is not correct.  It is missing the declaration of the variables i, j and the return statement.  Here is the corrected version:
vector<float> find_closest_elements(vector<float> numbers)
{
    vector<float> closest(2);
    for (int i = 0; i < numbers.size(); ++i)
        for (int j = i + 1; j < numbers.size(); ++j)
            if (abs(numbers[i] - numbers[j]) < abs(closest[0] - closest[1]))
            {
                closest[0] = numbers[i];
                closest[1] = numbers[j];
            }
    return closest;
}