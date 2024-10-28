
Your C++ code looks okay, but it's a bit hard to read due to lack of formatting and spacing. I suggest you take some time to clean it up. For example, you could format your code like this:
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold)
{
    for (int i = 0; i < numbers.size(); i++)
        for (int j = i + 1; j < numbers.size(); j++)
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
    for (int i = 0; i < paren_string.length(); i++)
    {
        chr = paren_string[i];
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
    return all_parens;
}

float