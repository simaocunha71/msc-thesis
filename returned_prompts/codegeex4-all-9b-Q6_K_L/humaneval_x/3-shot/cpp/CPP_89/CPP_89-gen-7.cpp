
The first function has_close_elements can be made more efficient with a single loop and a hash table.
Here is a version using a hash table:
#include <vector>
#include <cmath>
#include <unordered_set>

bool has_close_elements(const std::vector<float>& numbers, float threshold)
{
    std::unordered_set<float> seen;

    for (float n : numbers)
    {
        if (seen.find(n - threshold) != seen.end() || seen.find(n + threshold) != seen.end())
        {
            return true;
        }

        seen.insert(n);
    }

    return false;
}

The second function separate_paren_groups has a bug. If the input string ends with a closing parenthesis, it will be ignored. You need to add a check for the final level.
Here is a version that fixes this bug:
#include <vector>
#include <string>

std::vector<std::string> separate_paren_groups(const std::string& paren_string)
{
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;

    for (char chr : paren_string)
    {
        if (chr == '(')
        {
            ++level;
        }
        else if (chr == ')')
        {
            --level;
        }

        current_paren += chr;

        if (level == 0)
        {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }

    if (level != 0)
    {
        // The input string is not balanced
        throw std::runtime_error("Unbalanced parentheses");
    }

    return all_parens;
}

The third function truncate_number can be made more efficient with a single cast to int.
Here is a version that uses a cast to int:
#include <cmath>

float truncate_number(float number)
{
    return number - static_cast<int>(number);
}

The fourth function encrypt can be made more efficient with a single loop and a character array.
Here is a version that uses a character array:
#include <string>

std::string encrypt(const std::string& s)
{
    static const char* alphabet = "abcdefghijklmnopqrstuvwxyz";
    static