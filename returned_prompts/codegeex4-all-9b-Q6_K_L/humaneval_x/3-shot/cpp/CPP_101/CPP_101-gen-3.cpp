
Review of your code
1. Do not use using namespace std; in header files. It will make all the names from std visible everywhere and may cause name clashes. 
2. Your function names are in lower case. It's better to use camelCase for function names.
3. In has_close_elements, you can use auto for the loop variables, it will make the code shorter and more readable.
4. Your function names are not descriptive enough. It's better to use a name that describes what the function does.
5. Your function separate_paren_groups has a bug. It does not handle the case when the input string is empty.
6. In truncate_number, you can use static_cast<int>(number) instead of int(number).
7. In words_string, you can use std::find_if to find the first comma or space in the string.
8. In words_string, you can use std::istringstream to split the string into words.

Here is my version of your code:
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

bool has_close_elements(const vector<float>& numbers, float threshold) {
    for (auto i = 0u; i < numbers.size(); ++i) {
        for (auto j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
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
           