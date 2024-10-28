
Code organization
It's good to see you have a separate function for each of the questions, but it's not good to have them all in the same file. Try organizing your code as follows:
main.cpp
// ...

vector<string> separate_paren_groups(string paren_string);

// ...

int main() {
    // ...

    vector<string> result = separate_paren_groups("((()))");
    for (const auto& s : result) {
        cout << s << endl;
    }

    // ...
}

has_close_elements.cpp
// ...

#include <stdio.h>
#include <vector>
#include <cmath>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    // ...
}

// ...

has_close_elements.h
// ...

#pragma once

#include <vector>

bool has_close_elements(vector<float> numbers, float threshold);

// ...

This way, you can compile each function separately and have a clear separation of responsibilities.

Magic numbers
Your function has_close_elements compares two numbers with a threshold of 0.5. This is a magic number, and it's not clear what it means. You should use a named constant instead:
const float CLOSENESS_THRESHOLD = 0.5;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (auto i = 0u; i < numbers.size(); ++i) {
        for (auto j = i + 1u; j < numbers.size(); ++j) {
            if (std::abs(numbers[i] - numbers[j]) < CLOSENESS_THRESHOLD) {
                return true;
            }
        }
    }
    return false;
}

Naming conventions
Your function names use camelCase, but your variables use snake_case. Stick to one convention:
bool has_close_elements(vector<float> numbers, float threshold) {
    for (auto i = 0u; i < numbers.size(); ++i) {
        for (auto j = i + 1u; j < numbers.size(); ++j) {
            if (std::abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Also, don't use single-letter variable names. They're hard to understand and easy to confuse with constants.

C++ standard library
You're using the std namespace, but you