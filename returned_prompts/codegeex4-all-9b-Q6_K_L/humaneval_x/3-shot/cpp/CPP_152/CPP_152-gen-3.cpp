
There are a few things to point out here:

Use proper indentation to make the code more readable.
Use <algorithm> instead of <math.h> for the std::abs function.
The first question has a for loop that is iterating over all of the elements in the vector twice. You should be able to solve this question in one pass.
You can use std::string::push_back to append characters to a string.
You should be able to solve the third question in one line.
Your fourth question is not clear about what the "long-awaited event" is. Is it a sports match, a competition, or something else? That will affect the solution.

Here's a solution to the first question:
#include <algorithm>
#include <vector>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Here's a solution to the second question:
#include <vector>
#include <string>
using namespace std;

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            level++;
            current_paren.push_back(chr);
        } else if (chr == ')') {
            level--;
            current_paren.push_back(chr);
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Here's a solution to the third question:
#include <cmath>
using namespace std;

float truncate_number(float number) {
    return number - floor(number);
}

Here's a solution to the fourth question:
#include <vector>
#include <cmath>
using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    vector<int> result;
    for (int i = 0; i < game.size(); i++) {
        result