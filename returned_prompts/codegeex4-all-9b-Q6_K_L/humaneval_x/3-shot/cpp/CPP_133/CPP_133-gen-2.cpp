
I have no way of testing your code, so I can't verify that it's working. However, there are a few things you might want to consider.

Your code is very long and hard to read. You could try to make it more concise by using built-in functions and language features.
In the separate_paren_groups function, you are using a for loop and an if statement, but you could simplify your code by using a while loop and a switch statement.
In the sum_squares function, you are using a for loop and a math function, but you could simplify your code by using a for_each loop and an algorithm function.

Here's an example of how you might simplify your code:

#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

bool has_close_elements(std::vector<float> numbers, float threshold) {
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = i + 1; j != numbers.end(); ++j) {
            if (std::abs(*i - *j) < threshold) {
                return true;
            }
        }
    }
    return false;
}

std::vector<std::string> separate_paren_groups(std::string paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        switch (chr) {
            case '(':
                ++level;
                break;
            case ')':
                --level;
                if (level == 0) {
                    all_parens.push_back(current_paren);
                    current_paren.clear();
                }
                break;
        }
        current_paren += chr;
    }
    return all_parens;
}

float truncate_number(float number) {
    return std::fmod(number, 1.0f);
}

int sum_squares(std::vector<float> lst) {
    int sum = 0;
    std::transform(lst.begin(), lst.end(), std::back_inserter(sum), [](float x) {
        return static_cast<int>(std::ceil(x)) * static_cast<int>(std::ceil(x));
    });
