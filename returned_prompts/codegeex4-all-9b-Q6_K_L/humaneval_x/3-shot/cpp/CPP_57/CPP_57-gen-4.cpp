
has_close_elements()
The loop can be simplified by using a range-based for loop:
for (auto i = numbers.begin(); i != numbers.end(); ++i)
for (auto j = i + 1; j != numbers.end(); ++j)
    if (abs(*i - *j) < threshold)
        return true;

The second loop can be started with i+1, which is the same as the original code.  However, the second loop can be a range-based for loop as well, and the use of abs() is more C++-like than math.h::abs():
for (auto i = numbers.begin(); i != numbers.end(); ++i)
    for (auto j = i + 1; j != numbers.end(); ++j)
        if (std::abs(*i - *j) < threshold)
            return true;

separate_paren_groups()
The loop can be a range-based for loop:
for (auto chr : paren_string)
{
    if (chr == '(')
    {
        level += 1;
        current_paren += chr;
    }
    if (chr == ')')
    {
        level -= 1;
        current_paren += chr;
        if (level == 0)
        {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
}

truncate_number()
The use of math.h::abs() is more C++-like than math.h::abs():
return std::abs(number - int(number));

monotonic()
The loop can be a range-based for loop:
for (auto i = l.begin(); i != l.end(); ++i)
{
    if (i != l.begin())
    {
        if (*i < *(i - 1))
            c1 += 1;
        if (*i > *(i - 1))
            c2 += 1;
    }
}

if (c1 > 0 && c2 > 0)
    return false;
else
    return true;

The return false;