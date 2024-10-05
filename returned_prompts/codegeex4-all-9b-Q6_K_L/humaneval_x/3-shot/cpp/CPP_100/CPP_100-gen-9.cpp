
Your first question is a bit unclear.  What exactly are you comparing?  I'm assuming you're comparing the absolute difference between each pair of numbers, but that's not clear from your question.  You're also using an absolute value, which is good, but you could use a fabs() function.
You're also using a goto statement, which is generally a bad idea.  You can rewrite your loop without using it.
Here is a possible solution:
#include <cmath>
#include <vector>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (vector<float>::size_type i = 0; i < numbers.size(); i++)
        for (vector<float>::size_type j = i+1; j < numbers.size(); j++)
            if (fabs(numbers[i] - numbers[j]) < threshold)
                return true;

    return false;
}

Your second question is a bit unclear as well.  You're looking for parenthetical groups, but you're not checking to make sure that they are balanced.  You're also not ignoring spaces.  This is a good thing, though, since you're ignoring them in your example.  You're also using a goto statement, which is a bad idea.  You can rewrite your loop without using it.
Here is a possible solution:
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    size_t i;

    for (i = 0; i < paren_string.length(); i++)
    {
        switch (paren_string[i])
        {
        case '(':
            level++;
            current_paren += paren_string[i];
            break;
        case ')':
            level--;
            current_paren += paren_string[i];
            if (level == 0)
            {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
            break;
        default:
            //