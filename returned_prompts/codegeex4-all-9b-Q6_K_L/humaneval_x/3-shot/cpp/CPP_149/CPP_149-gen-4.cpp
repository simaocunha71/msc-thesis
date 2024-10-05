
C++ has a standard library for manipulating vectors. In your code, you're using a for loop to iterate over a vector. This is unnecessary and inefficient. You should use the built-in iterators instead. 
Here's the code for your first function with a few other improvements:
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool has_close_elements(const vector<float>& numbers, float threshold)
{
    auto it = numbers.begin();
    while (it != numbers.end())
    {
        auto it2 = it + 1;
        while (it2 != numbers.end())
        {
            if (abs(*it - *it2) < threshold)
            {
                return true;
            }
            ++it2;
        }
        ++it;
    }

    return false;
}

I've also replaced the for loop with a while loop and changed the variable names to be more descriptive. I've also added const to the vector parameter to indicate that the function won't modify the vector. I've also added the using namespace std; line to avoid prefixing standard library names with std::.
Your second function is fine, except for the fact that you're using a for loop to iterate over the string. Here's the modified code:
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> separate_paren_groups(const string& paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;

    for (char c : paren_string)
    {
        if (c == '(')
        {
            ++level;
        }
        else if (c == ')')
        {
            --level;
        }

        current_paren += c;

        if (level == 0)
        {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }

    return all_parens;
}

I've replaced the for loop with a range-based for loop and changed the variable names to be more descriptive. I've also added const to the string parameter to indicate that the function won't modify the string.
Your third function is fine