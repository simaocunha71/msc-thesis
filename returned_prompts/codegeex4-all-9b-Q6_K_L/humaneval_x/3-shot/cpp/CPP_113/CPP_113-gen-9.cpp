
There are a few issues here. First off, the functions don't have a return type, so you need to specify that the functions return a bool, vector<string>, float, or vector<string> respectively. Second, the functions aren't defined in the global scope. You need to define them within a namespace, like std::, or define them at the top level of your program.
Here are the corrected versions of your functions:
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    int i, j;
    for (i = 0; i < numbers.size(); i++)
        for (j = i + 1; j < numbers.size(); j++)
            if (abs(numbers[i] - numbers[j]) < threshold)
                return true;
    return false;
}

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for (i = 0; i < paren_string.length(); i++) {
        chr = paren_string[i];
        if (chr == '(') {
            level += 1;
            current_paren += chr;
        }
        if (chr == ')') {
            level -= 1;
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
    return number - int(number);
}

vector<string> odd_count(vector<string> lst) {
    vector<string> all_odd;
    string str = "";
    int i, j;
    for (i