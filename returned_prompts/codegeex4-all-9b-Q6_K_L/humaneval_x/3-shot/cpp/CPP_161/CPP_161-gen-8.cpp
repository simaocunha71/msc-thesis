
has_close_elements
Your code is correct, but it's not efficient. You're iterating over the entire array twice, which can be reduced to a single pass. You can use the fact that your array is sorted (if it was) to optimize it further.
Also, your variable names are not very descriptive. I'd suggest using names like:
const float EPSILON = 1e-6f;
for (size_t i = 0; i < numbers.size() - 1; ++i)
{
    if (fabs(numbers[i + 1] - numbers[i]) < EPSILON)
    {
        return true;
    }
}

separate_paren_groups
Your code is correct, but it's not very efficient. You're iterating over the entire string once, which can be reduced to a single pass. You can use a stack to keep track of the current level of parentheses.
Also, your variable names are not very descriptive. I'd suggest using names like:
vector<string> separate_paren_groups(const string &paren_string)
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
Your code is correct, but it's not very efficient. You can use the floor function to get the integer part of the number, and then subtract it from the original number.
Also,