
A few minor things that could be improved:

Use standard library functions where possible. For example, you are using std::atoi() to convert strings to integers. Instead, you can use std::stoi(), which throws a std::invalid_argument if the string is not a valid integer representation.
The variable names are all very generic. For example, chr could be more descriptive, such as character. Also, i could be more descriptive, such as index.
You are using the ternary operator in a couple of places. Instead, you can use an if-else statement, which is more readable and easier to understand.
You are using a hard-coded value of 0.3 in the has_close_elements() function. Instead, you should use a named constant, such as const float threshold = 0.3;.
Your code lacks comments. Comments are important for explaining what your code does, especially for complex functions.
Your code lacks error handling. For example, in the simplify() function, you are assuming that the input strings are valid fractions. However, there is no error handling for invalid input strings.
Your code lacks documentation. For example, the separate_paren_groups() function lacks a description of what it does and what the input and output are.

Here is a revised version of your code:

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

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

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
   