
Firstly, you need to include the necessary headers and use the correct namespace. Also, you need to check for the validity of the inputs. I'll provide code for all the questions.

Question 1: Check if in given vector of numbers, are any two numbers closer to each other than given threshold.

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    // Check for empty vector
    if (numbers.empty()) {
        return false;
    }

    // Sort the vector
    sort(numbers.begin(), numbers.end());

    // Check for numbers within the threshold
    for (int i = 0; i < numbers.size() - 1; i++) {
        if (numbers[i + 1] - numbers[i] < threshold) {
            return true;
        }
    }

    return false;
}

Question 2: Separate groups of nested parentheses into separate strings and return the vector of those.

#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    stack<char> s;
    string current_paren;
    int i;

    for (i = 0; i < paren_string.length(); i++) {
        if (paren_string[i] == '(') {
            s.push(paren_string[i]);
        } else if (paren_string[i] == ')') {
            if (!s.empty()) {
                s.pop();
                current_paren += paren_string[i];
                if (s.empty()) {
                    all_parens.push_back(current_paren);
                    current_paren = "";
                }
            }
        }
    }

    return all_parens;
}

Question 3: Return the decimal part of the number.

#include <iostream>
#include <cmath>

using namespace std;

float truncate_number(float number){
    return number - (int)number;
}

Question 4: Multiply the unit digits of two numbers.

#include <iostream>
#include <cmath>

using namespace std;

int multiply(int a, int b){
    return abs(a % 10) * abs(b % 10);
}