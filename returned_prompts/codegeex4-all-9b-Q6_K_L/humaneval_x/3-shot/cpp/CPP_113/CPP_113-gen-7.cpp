
has_close_elements

You have an infinite loop because you don't have a break condition.  You also have a redundant test.  If you have a break condition, you don't need to return false at the end.  This should be:
for (i=0; i<numbers.size(); i++)
{
    for (j=i+1; j<numbers.size(); j++)
    {
        if (abs(numbers[i]-numbers[j]) < threshold)
        {
            return true;
        }
    }
}

separate_paren_groups

This works, but it's not very efficient.  You could do it in a single pass, but it would be more complicated.  You could also make it more efficient by removing the calls to push_back and +=.  This should be:
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

truncate_number

This works, but it's not very efficient.  You could do it in a single line of code.  This should be:
return number - floor(number);

odd_count

This is not the best way to solve the problem.  The easiest way to solve the problem is to use an STL algorithm.  This should be:
#include <algorithm>
#include <string>

vector<string> odd_count(vector<string> lst)
{
    vector<string> all_odd;
    for_each(lst.begin(), lst.end(), [&all_odd](const string &str)
    {
        string current_str;
        for_each(str.begin(), str.end(), [&current_str](