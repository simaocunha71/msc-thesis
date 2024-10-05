
has_close_elements
There are a few things that could be improved:

You've got an un-named label A, which is a bad practice. If you need to jump out of a nested loop, use break.
You're calling abs() but it's not necessary. The difference between two floating point numbers is either positive or negative, so you can just use the difference directly.
You're not checking whether numbers is empty, which will result in undefined behaviour.

Here's an improved version:
bool has_close_elements(vector<float> numbers, float threshold)
{
    for (size_t i = 0; i < numbers.size(); i++)
        for (size_t j = i + 1; j < numbers.size(); j++)
            if (numbers[i] - numbers[j] < threshold || numbers[j] - numbers[i] < threshold)
                return true;
    return false;
}

separate_paren_groups
This function is fine, but it could be more efficient. You're iterating through the string twice: once to build the current_paren string, and then again to add it to all_parens. You could do both in one loop:
vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string)
    {
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

truncate_number
This function is fine, but it could be more efficient. You're using int() to truncate the number, but you could use a simple cast instead:
float truncate_number(float number)
{
    return number - static_cast<float