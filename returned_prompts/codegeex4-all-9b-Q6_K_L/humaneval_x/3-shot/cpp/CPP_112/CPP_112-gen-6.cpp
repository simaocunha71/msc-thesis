
Your first function works just fine.  But there's a more efficient way to do it:
#include <algorithm>
#include <vector>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold)
{
    if (numbers.size() < 2) return false;

    sort(numbers.begin(), numbers.end());

    for (size_t i = 1; i < numbers.size(); ++i)
    {
        if (numbers[i] - numbers[i - 1] < threshold)
            return true;
    }

    return false;
}

You were correct to iterate over all pairs, but you could have done it more efficiently by sorting the numbers first.  Then you only need to check adjacent pairs, which is a lot fewer checks.
Your second function also works, but you don't need the level variable:
#include <vector>
#include <string>

using namespace std;

vector<string> separate_paren_groups(string paren_string)
{
    vector<string> all_parens;
    string current_paren;
    char chr;

    for (size_t i = 0; i < paren_string.length(); ++i)
    {
        chr = paren_string[i];

        if (chr == '(')
        {
            current_paren += chr;
        }
        else if (chr == ')')
        {
            current_paren += chr;
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }

    return all_parens;
}

Your third function works, but it's a bit more complicated than it needs to be:
#include <cmath>

float truncate_number(float number)
{
    return number - int(number);
}

You don't need the if statement.  The conversion to int truncates the value, so you don't need to subtract it from the original value.
Your fourth function has a bug:
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<string> reverse_delete(string s, string