
Q1: has_close_elements
In this question, you are iterating over each pair of elements in the vector. This can be optimized to iterate over each element only once and keep track of the smallest and largest elements seen so far. If the difference between the smallest and largest is less than the threshold, then you can return true. Otherwise, you can update the smallest and largest and continue.
#include <vector>
#include <cmath>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    float min = numbers[0];
    float max = numbers[0];
    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i] < min) {
            min = numbers[i];
        }
        if (numbers[i] > max) {
            max = numbers[i];
        }
        if (max - min < threshold) {
            return true;
        }
    }
    return false;
}

Q2: separate_paren_groups
In this question, you are iterating over each character in the string and keeping track of the current group of parentheses. When you encounter a closing parenthesis, you check if the level is 0. If it is, then you have found the end of a group and you can add it to the vector of groups. Otherwise, you continue to iterate over the string.
#include <vector>
#include <string>
using namespace std;

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
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
    }
    return all_parens;
}

Q3: truncate_number
In this question, you are simply subtracting the integer part of the number from the number itself. This can be done using the built-in floor