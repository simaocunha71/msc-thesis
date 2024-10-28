
First of all, you're not using any of the standard library containers and algorithms available to you.  You should be using std::vector and std::abs instead of std::vector<float> and std::abs(float).  Same with the other questions.
You've also got a missing closing brace on your first question.

Your first function doesn't need a label A, and the variable i and j should be declared in the for loop.
Your second function needs braces around the for loop, and current_paren should be initialized to an empty string.
Your third function has a redundant cast to float.  You can just return number - int(number).
Your fourth function has a redundant cast to float.  You can just return (a+b+c)/2.0 - floor((a+b+c)/2.0).
Your fifth function has a redundant cast to float.  You can just return (a+b+c)/2.0 - floor((a+b+c)/2.0).

Here's your code with the issues fixed:
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    for (std::size_t i = 0; i < numbers.size(); ++i)
        for (std::size_t j = i + 1; j < numbers.size(); ++j)
            if (std::abs(numbers[i] - numbers[j]) < threshold)
                return true;

    return false;
}

std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    char chr;
    for (std::size_t i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];
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
       