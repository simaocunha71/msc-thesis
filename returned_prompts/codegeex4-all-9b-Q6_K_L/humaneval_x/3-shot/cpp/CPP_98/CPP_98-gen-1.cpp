
has_close_elements() is not complete. You have to initialize i and j before using them in the for loops. You are also missing a semicolon (;) after the return true in the if statement.
separate_paren_groups() is not complete. You are not checking whether the character is a space before adding it to the current_paren string. The first group of parentheses is not correctly identified. You have to add a space before adding the current_paren to all_parens when it is not empty.
truncate_number() is not complete. You are not returning anything.
count_upper() is not complete. You are not returning anything.

Here is the corrected code:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    int i, j;
    for (i = 0; i < numbers.size(); i++) {
        for (j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
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
        } else if (chr == ')') {
            level -= 1;
            current_paren += chr;
            if (level == 0 && !current_paren.empty()) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

float truncate_number(float number) {
    return number - floor(number);
}

int count_upper(string s) {
    string upper = "AEIOU";
    int i;
    int count =