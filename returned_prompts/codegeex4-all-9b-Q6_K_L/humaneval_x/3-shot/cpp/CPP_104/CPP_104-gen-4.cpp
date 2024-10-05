
A few minor points:

In has_close_elements, the name has_close_elements is a bit misleading. It would be more descriptive to call it something like has_pair_within_threshold.
In has_close_elements, you should consider using iterators instead of the index variables i and j. This will make the code a bit more readable and will also avoid the need for the index variables. For example:
for (auto it = numbers.begin(); it != numbers.end(); ++it)
{
    for (auto it2 = it + 1; it2 != numbers.end(); ++it2)
    {
        if (abs(*it - *it2) < threshold)
        {
            return true;
        }
    }
}
return false;

In separate_paren_groups, you should consider using a stringstream instead of concatenating strings with the + operator. This will make the code more efficient and will also avoid the need for the string variable current_paren. For example:
stringstream ss;
for (int i = 0; i < paren_string.length(); i++)
{
    chr = paren_string[i];
    if (chr == '(')
    {
        level += 1;
        ss << chr;
    }
    else if (chr == ')')
    {
        level -= 1;
        ss << chr;
        if (level == 0)
        {
            all_parens.push_back(ss.str());
            ss.str("");
        }
    }
}

In truncate_number, you should consider using the fmod function instead of the int conversion. This will make the code more accurate and will also avoid the need for the int conversion. For example:
return fmod(number, 1.0f);

In unique_digits, you should consider using the std::remove_if function instead of a manual loop. This will make the code more efficient and will also avoid the need for the index variable i. For example:
unique_digits.erase(std::remove_if(unique_digits.begin(), unique_digits.end(), [](int num) {
    while (num > 0