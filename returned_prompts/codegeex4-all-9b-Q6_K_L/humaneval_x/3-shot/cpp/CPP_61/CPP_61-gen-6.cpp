
Q1: has_close_elements

This function could be more efficient by avoiding the nested loop.  Instead, it would be simpler to sort the input vector and then just check the adjacent pairs.  This would require a copy of the vector, but this would be necessary in any case since the function is required to return a boolean value.  There are other ways to achieve this, such as returning an iterator, but that would still require a copy of the vector.
Here's how it would look:
bool has_close_elements(vector<float> numbers, float threshold)
{
    sort(numbers.begin(), numbers.end());
    for (size_t i = 1; i < numbers.size(); ++i)
    {
        if (numbers[i] - numbers[i-1] < threshold)
            return true;
    }
    return false;
}

Q2: separate_paren_groups

There is no need to maintain the current_paren string as a string.  It is simpler and more efficient to just keep track of the current level of parentheses.  This can be done with an integer variable.  When the level reaches zero, a new string can be started.  Here's how it would look:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    int level = 0;
    int i;
    for (i = 0; i < paren_string.length(); i++)
    {
        if (paren_string[i] == '(')
            level += 1;
        else if (paren_string[i] == ')')
            level -= 1;
        if (level == 0)
            all_parens.push_back(string(paren_string.begin() + all_parens.size() * 2, paren_string.begin() + i + 1));
    }
    return all_parens;
}

Q3: truncate_number

This function can be simplified by using the fmod function from the math library.  This function returns the remainder of the division of the two operands, which is exactly what is needed here. 