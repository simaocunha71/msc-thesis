
has_close_elements
You are not using the vector numbers, just iterating over the range [0, numbers.size()).
You can use range based for loop to avoid the index variables i and j.
#include<vector>

bool has_close_elements(vector<float> numbers, float threshold) {
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i + 1; j != numbers.end(); ++j) {
            if (abs(*i - *j) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
Your code does not handle the case where the string ends with a '('.
To fix this, you can use a flag to determine if you are currently in a group.
#include<vector>
#include<string>

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    bool in_group = false;
    for (auto chr : paren_string) {
        if (chr == '(') {
            in_group = true;
        }
        if (in_group) {
            current_paren += chr;
        }
        if (chr == ')') {
            in_group = false;
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
    return all_parens;
}

truncate_number
Your code is correct, but you can use the fmod function to truncate the number.
#include<cmath>

float truncate_number(float number) {
    return fmod(number, 1.0);
}

sort_numbers
Your code does not handle the case where the string contains invalid numbers.
To fix this, you can use a map to store the numbers and iterate over the string to find the numbers.
#include<map>
#include<sstream>
#include<algorithm>

string sort_numbers(string numbers) {
    map<string, int> number_map = {
        {"zero", 0},
        {"one", 1},
        {"