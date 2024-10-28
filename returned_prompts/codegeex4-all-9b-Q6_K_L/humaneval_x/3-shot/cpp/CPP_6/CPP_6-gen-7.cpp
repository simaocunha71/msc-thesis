
has_close_elements
The algorithm is correct, but could be improved by using iterators instead of indices:
for (auto i = numbers.begin(); i != numbers.end(); ++i)
{
    for (auto j = i + 1; j != numbers.end(); ++j)
    {
        if (abs(*i - *j) < threshold)
        {
            return true;
        }
    }
}
return false;

The current implementation has a time complexity of O(n^2), but it can be reduced to O(n log n) by sorting the vector first:
sort(numbers.begin(), numbers.end());
for (auto i = numbers.begin(); i != numbers.end(); ++i)
{
    auto j = upper_bound(numbers.begin(), numbers.end(), *i + threshold);
    if (j != numbers.end() && *j - *i < threshold)
    {
        return true;
    }
}
return false;

separate_paren_groups
The algorithm is correct, but it can be improved by using a stringstream to parse the string instead of iterating over its characters:
stringstream ss(paren_string);
string current_paren;
int level = 0;
string paren_group;
while (ss >> paren_group)
{
    for (char c : paren_group)
    {
        if (c == '(')
        {
            level += 1;
        }
        else if (c == ')')
        {
            level -= 1;
        }
        if (level == 0)
        {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
        else
        {
            current_paren += c;
        }
    }
}
return all_parens;

truncate_number
The algorithm is correct, but