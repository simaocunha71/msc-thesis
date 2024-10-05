
First, don't use using namespace std; It's bad practice. You can use std::vector and std::string instead of vector and string. Also, instead of including <math.h>, use <cmath> (the math.h is deprecated).
Second, you're missing the closing brace on your find_closest_elements function. You should also use the initializer list to initialize your vector:
vector<float> min_numbers = {numbers[i], numbers[j]};

Lastly, your find_closest_elements function doesn't actually return two elements. It returns a vector with two elements. You should return the elements directly:
return {numbers[i], numbers[j]};

Here's your updated code:
#include <vector>
#include <string>
#include <cmath>

bool has_close_elements(std::vector<float> numbers, float threshold)
{
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        for (size_t j = i + 1; j < numbers.size(); ++j)
        {
            if (std::abs(numbers[i] - numbers[j]) < threshold)
            {
                return true;
            }
        }
    }

    return false;
}

std::vector<std::string> separate_paren_groups(std::string paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    char chr;
    size_t i;

    for (i = 0; i < paren_string.length(); ++i)
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
        }
    }

    return all_parens;
}

float truncate