
For your first code block, you should use the standard library function std::abs:
#include <cmath> // std::abs

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (auto i = begin(numbers); i != end(numbers); ++i)
    {
        for (auto j = i + 1; j != end(numbers); ++j)
        {
            if (std::abs(*i - *j) < threshold)
            {
                return true;
            }
        }
    }
    return false;
}

Note that I replaced the manual loop indexing with iterators.

Your second code block seems fine, but I would write it as follows to make it more readable:
vector<string> separate_paren_groups(string paren_string)
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
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Your third code block is fine, but I would write it like this:
float truncate_number(float number)
{
    return number - std::floor(number);
}

The fourth code block can be written like this:
int specialFilter(vector<int> nums)
{
    int count = 0;
    for (int num : nums)
    {
        if (num > 10 && std::abs(num / 10) % 2 == 1 && std::abs(num % 10) % 2 == 1)
        {
            ++count;
        }
    }
    return count;
}

I would also recommend not using the using namespace std; directive, as it can lead to name conflicts.