
The first thing I see is the lack of braces around the for loop in both functions. I'd expect the functions to be defined as:
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

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;

    for (i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];

        if (chr == '(')
        {
            level += 1;
            current_paren += chr;
        }
        else if (chr == ')')
        {
            level -= 1;
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

The second thing I notice is that the second function doesn't handle the case where there are unbalanced parentheses in the string. I'd expect a function like this to handle that case as well.
The third thing I notice is that you're not using the truncate_number function. I'd expect you to use this function in the sum_squares function. I'd suggest something like this:
int sum_squares(vector<float> lst)
{
    int sum = 0;

    for (float number : lst)
        sum += ceil(number) * ceil(number);

    return sum;
}

Finally, it's worth mentioning that the truncate_number function isn't doing what you expect. You're truncating the number, but you're not returning the truncated number. I'd expect this function to return the fractional part of the number.
I hope this helps. If you have any further questions, please let me know.