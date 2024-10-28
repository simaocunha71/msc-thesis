
Code formatting
Your code is poorly formatted, making it hard to read.  Fix it!  Here's a start:

/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
true
*/
#include <vector>
#include <cmath>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups("( ) (( )) (( )( ))")
{"()", "(())", "(()())"}
*/
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(string paren_string) {
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
            if (level == 0