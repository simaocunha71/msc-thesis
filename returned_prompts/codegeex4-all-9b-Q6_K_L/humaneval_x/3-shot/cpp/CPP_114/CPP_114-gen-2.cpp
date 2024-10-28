
for (auto i = 0u; i < numbers.size(); i++)
    for (auto j = i + 1; j < numbers.size(); j++)
        if (abs(numbers[i] - numbers[j]) < threshold)
            return true;

return false;

Your second function is also correct. You could use auto for the variable i, and use std::accumulate to simplify the calculation of the level. Also, it's better to use std::string::empty() to check if the string is empty.

for (auto i = 0u; i < paren_string.length(); i++)
{
    chr = paren_string[i];
    if (chr == '(')
    {
        level++;
        current_paren += chr;
    }
    if (chr == ')')
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

Your third function is correct too. The only thing I would suggest is to use static_cast<int>(number) instead of int(number).

return number - static_cast<int>(number);

Your fourth function is wrong. The minimum sum of a sub-vector can be achieved by summing up all the negative numbers and positive numbers separately, and then subtracting the smaller sum from the larger one. You should also initialize current_sum to 0 at the beginning of the loop.

long long min_sum = LLONG_MAX;
long long current_sum = 0;
long long positive_sum = 0;
long long negative_sum = 0;
int i;
for (i = 0; i < nums.size(); i++)
{
    if (nums[i] >= 0)
        positive_sum += nums[i];
    else
        negative_sum += nums[i];
}

if (positive_sum < negative_sum)
