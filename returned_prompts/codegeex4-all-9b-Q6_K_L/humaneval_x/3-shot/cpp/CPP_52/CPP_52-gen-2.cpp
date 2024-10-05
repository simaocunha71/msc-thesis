
You've got a few issues with your code:

Your code is missing a closing brace for your has_close_elements function. Your main function, separate_paren_groups, and truncate_number.  This is most likely a copy/paste error.
Your separate_paren_groups function doesn't handle the case where there is no space between two parentheses. The way you handle spaces could potentially cause unexpected results.
In your separate_paren_groups function, you never decrement the level if you encounter a space.  This could cause your function to fail if there is a space within a parenthetical group.
In your truncate_number function, you are using the int() cast operator, which will truncate towards zero.  This may not give the result you expect for negative numbers.

Here's a revised version of your code that addresses these issues:

#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold)
{
    int i, j;
    for (i = 0; i < numbers.size(); i++)
    {
        for (j = i + 1; j < numbers.size(); j++)
        {
            if (abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
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
    for (i = 0; i < paren_string.length(); i++)
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
                current_paren = "";
            }
        }
        else if (chr != ' ')
        {
            // This handles the case where there is no space between two parentheses.
            current_paren += chr;
        }
    }
    return all_parens;
}

float truncate_number(float number)
{
    return number - floor(number);
}

bool below_threshold