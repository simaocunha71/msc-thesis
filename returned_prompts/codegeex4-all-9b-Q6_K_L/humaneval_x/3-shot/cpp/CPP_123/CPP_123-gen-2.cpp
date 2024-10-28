
Firstly, in all of these functions, you should pass your parameters by reference. This will avoid copying the data, and will save memory, especially if you have large data. Secondly, you could use auto, to make the code shorter and easier to read.

Here's a cleaned-up version of your first function:

```cpp
#include <vector>
#include <cmath>

using namespace std;

bool has_close_elements(const vector<float>& numbers, float threshold)
{
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        for (size_t j = i + 1; j < numbers.size(); ++j)
        {
            if (abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }

    return false;
}
```

Here's a cleaned-up version of your second function:

```cpp
#include <vector>
#include <string>

using namespace std;

vector<string> separate_paren_groups(const string& paren_string)
{
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    size_t i;

    for (i = 0; i < paren_string.size(); ++i)
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
                current_paren.clear();
            }
        }
    }

    return all_parens;
}
```

Here's a cleaned-up version of your third function:

```cpp
#include <cmath>

float truncate_number(float number)
{
    return number - static_cast<int>(number);
}
```

Here's a cleaned-up version of your fourth function:

```cpp
#include <vector>
#include <algorithm