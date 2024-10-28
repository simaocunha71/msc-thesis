
There are a few things you can do to make your code more efficient and clean.
has_close_elements
You could use a set to store the numbers and then check if any two numbers are in the set with a difference less than the threshold. This would improve the time complexity from O(n^2) to O(n log n).
separate_paren_groups
You could use a stack to keep track of the parentheses. When you encounter a closing parenthesis, you could pop the stack until you find the matching opening parenthesis. This would improve the time complexity from O(n^2) to O(n).
truncate_number
You could use the fmod function to get the fractional part of the number. This would improve the time complexity from O(1) to O(1).
digits
You could use the isdigit function to check if a character is a digit. This would improve the time complexity from O(n) to O(n).
Here is the updated code:
has_close_elements
#include <unordered_set>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    unordered_set<float> numbers_set(numbers.begin(), numbers.end());
    for (float num : numbers) {
        for (float num2 : numbers_set) {
            if (abs(num - num2) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
#include <stack>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    stack<char> paren_stack;
    for (char chr : paren_string) {
        if (chr == '(') {
            paren_stack.push(chr);
            current_paren += chr;
        } else if (chr == ')') {
            paren_stack.pop();
            current_paren += chr;
            if (paren_stack.empty()) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

truncate_number
#include <cmath>

float truncate_number(float number) {
   