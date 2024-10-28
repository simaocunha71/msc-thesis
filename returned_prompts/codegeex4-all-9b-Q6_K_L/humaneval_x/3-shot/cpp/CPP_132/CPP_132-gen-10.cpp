
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Check if in given vector of numbers, are any two numbers closer to each other than given threshold.
bool has_close_elements(vector<float> numbers, float threshold) {
    for (size_t i = 0; i < numbers.size(); i++) {
        for (size_t j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

// Input to this function is a string containing multiple groups of nested parentheses. 
// Your goal is to separate those group into separate strings and return the vector of those.
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            level += 1;
        } else if (chr == ')') {
            level -= 1;
        }
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }
    return all_parens;
}

// Given a positive floating point number, it can be decomposed into and integer part 
// (largest integer smaller than given number) and decimals (leftover part always smaller than 1).
float truncate_number(float number) {
    return number - static_cast<int>(number);
}

// Create a function that takes a string as input which contains only square brackets. 
// The function should return true if and only if there is a valid subsequence of brackets 
// where at least one bracket in the subsequence is nested.
bool is_nested(string str) {
    int level = 0;
    for (char chr : str) {
        if (chr == '[') {
            level += 1;
        } else if (chr == ']') {
            level -= 1;
