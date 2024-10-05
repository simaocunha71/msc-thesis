
Q1:
This is a correct solution, but it can be optimized. The inner loop can start from the next index of the outer loop.
#include <cmath>
#include <vector>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Q2:
This is a correct solution, but it can be optimized. You can use a stack to keep track of the current level of parentheses. When you encounter a closing parenthesis, you can check if the current level is the same as the stack's top element.
#include <string>
#include <vector>
using namespace std;

vector<string> separate_paren_groups(string paren_string){
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
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Q3:
This is a correct solution, but it can be optimized. You can use the modulus operator to calculate the decimal part of the number.
#include <cmath>
using namespace std;

float truncate_number(float number){
    return number - int(number);
}

Q4:
This is a correct solution, but it can be optimized. You can use a sliding window to check if the second word or any of its rotations is a