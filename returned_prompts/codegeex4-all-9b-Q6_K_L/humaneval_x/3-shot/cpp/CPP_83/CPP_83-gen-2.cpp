
Your solutions seem to be working correctly, but I would like to point out a few things.

For has_close_elements, you could potentially avoid the extra if statement, and return true immediately when the condition is met. This would avoid a potential expensive loop that is not needed.

    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;

Could be written as:
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
        return true;

    return false;

In separate_paren_groups, you are not checking to make sure the input string is valid. You could add a check to make sure the string only contains parentheses.

    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr!='(' && chr!=')')
            return all_parens;
    }

In truncate_number, you could use the fmod function to get the decimal part of the number.

    return fmod(number, 1);

In starts_one_ends, you could use pow to calculate the range of numbers to check. This would avoid a potential expensive loop that is not needed.

    return pow(10, n) - 1 - (pow(10, n-1) - 1) * 2;