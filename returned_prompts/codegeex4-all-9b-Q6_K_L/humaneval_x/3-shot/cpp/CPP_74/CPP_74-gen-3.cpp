
This is your first time posting a question here so I will try to give you as much help as possible.
First of all, it would be helpful if you would show your results so we can see if there is a problem with your code or with the question itself. In any case, I will try to help you.
Your first function has_close_elements looks fine to me. You could make it more efficient though by using the standard library algorithm std::min_element, which returns an iterator to the smallest element in the range [first, last).
Here is the new version of the function:
#include <algorithm>

bool has_close_elements(vector<float> numbers, float threshold) {
    auto min = std::min_element(numbers.begin(), numbers.end());
    auto max = std::max_element(numbers.begin(), numbers.end());
    return *max - *min < threshold;
}

Your second function separate_paren_groups has a bug. The condition level == 0 is not sufficient to detect when a group ends. You need to check if the current level is 0 and there are no more characters in the string. Otherwise, you will end up adding a group with one less parenthesis than it should have.
Here is the corrected version of the function:
#include <sstream>

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    int i = 0;
    while (i < paren_string.length()) {
        char chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
        i++;
    }
    return all_parens;
}

Your third function truncate_number is also fine. Just a minor suggestion, you could use static_cast<int> instead of int(number) to avoid the unnecessary