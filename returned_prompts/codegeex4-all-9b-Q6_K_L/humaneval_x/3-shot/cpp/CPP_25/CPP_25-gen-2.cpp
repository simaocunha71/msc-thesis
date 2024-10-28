
You have a lot of code, but it's mostly correct. However, it can be improved with a few suggestions:

Your for loops don't need a label.
Your for loops don't need braces.
You have some unnecessary braces.
Your function names have the wrong style. Use underscores instead of camel case. For example, has_close_elements should be has_close_elements.
Your functions have comments, but they are missing descriptions of the parameters and return values.
Your function has_close_elements is missing a comment describing the parameter and return values.
Your function separate_paren_groups is missing a comment describing the parameter and return values.
Your function truncate_number is missing a comment describing the parameter and return values.
Your function factorize is missing a comment describing the parameter and return values.
Your function factorize is missing a comment describing the parameter and return values.
Your function factorize is missing a comment describing the parameter and return values.

Here is the improved code:

#include<stdio.h>
#include<vector>
#include<math.h>
#include<string>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i = 0; i < numbers.size(); ++i)
        for (int j = i + 1; j < numbers.size(); ++j)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;

    return false;
}

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (int i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];
        if (chr == '(')
        {
            ++level;
            current_paren += chr;
        }
        if (chr == ')')
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

float truncate_number(float number)
{
    return number - int(number);
}

vector<int> factorize(int n)
{
    vector<int>