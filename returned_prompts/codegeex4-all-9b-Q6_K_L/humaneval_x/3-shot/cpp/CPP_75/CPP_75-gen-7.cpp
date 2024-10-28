
has_close_elements
This function is good, but you could make it more efficient by only considering numbers[i] and numbers[j] where i < j.  That would reduce the number of iterations by half.  Also, you could return false immediately if abs(numbers[i] - numbers[j]) >= threshold, instead of doing a return true at the end.
Also, you should avoid using a label (A) to jump to the beginning of a loop.  This is not good practice.  Instead, you should use a while loop that continues until the condition is met.  This would make your code more readable and maintainable.
Here's a revised version of your function:
bool has_close_elements(vector<float> numbers, float threshold){
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
This function is good, but you could make it more efficient by using a stack to keep track of the parentheses.  This would reduce the number of iterations required to separate the groups.  Also, you could use a string stream to build the current_paren string, instead of concatenating characters.
Here's a revised version of your function:
#include <sstream>

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    stringstream current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
            current_paren << chr;
        } else if (chr == ')') {
            --level;
            current_paren << chr;
            if (level == 0) {
                all_parens.push_back(current_paren.str());
                current_paren.str("");
            }
        }
    }
    return all_parens;
}

truncate_number
This function is good, but you could make it more efficient by using the modf function to