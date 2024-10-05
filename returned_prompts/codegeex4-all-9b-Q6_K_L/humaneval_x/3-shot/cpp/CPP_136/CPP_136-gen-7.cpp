
I have some suggestions for your code:

Use consistent formatting.
Use consistent naming conventions.
Avoid using namespace std;.
Don't use using namespace std; in headers.
Use braces {} for all control statements.
Use for (auto it : container) instead of for (int i=0; i<container.size(); i++).

Here's the refactored code:
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>

using std::vector;
using std::string;

bool has_close_elements(const vector<float>& numbers, float threshold) {
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        for (auto it2 = it + 1; it2 != numbers.end(); ++it2) {
            if (std::abs(*it - *it2) < threshold) {
                return true;
            }
        }
    }
    return false;
}

vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    for (size_t i = 0; i < paren_string.length(); ++i) {
        chr = paren_string[i];
        if (chr == '(') {
            ++level;
            current_paren += chr;
        } else if (chr == ')') {
            --level;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

float truncate_number(float number) {
    return number - static_cast<int>(number);
}

vector<int> largest_smallest_integers(const vector<int>& lst) {
    int neg = 0;
    int pos = 0;
    for (const auto& i : lst) {
        if (i > 0) {
            pos = i;
        }