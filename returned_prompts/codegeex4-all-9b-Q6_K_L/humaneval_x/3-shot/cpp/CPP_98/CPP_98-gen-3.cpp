
The first question is solved correctly, but there are some optimizations that could be done:

You don't need a label A: to return from within a function. You can simply use return true; or return false;
You can use the range-based for loop to iterate over the vector:
for (auto const& number : numbers) {
    for (auto const& other_number : numbers) {
        if (number == other_number) continue;
        if (abs(number - other_number) < threshold) return true;
    }
}
return false;

This will make the code more readable and easier to maintain.
The second question is also solved correctly, but again, there are some optimizations that could be done:

You don't need to use a char variable to store the current character. You can directly use paren_string[i];
You can use the range-based for loop to iterate over the vector:
for (auto const& chr : paren_string) {
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

This will make the code more readable and easier to maintain.
The third question is also solved correctly, but again, there are some optimizations that could be done:

You don't need to use the math.h library. You can use the fmodf function from the cmath library:
#include <cmath>

float truncate_number(float number) {
    return fmodf(number, 1);
}

This will make the code more readable and easier to maintain.
The fourth question is also solved correctly, but again, there are some optimizations that could be done:

You don't need to use the algorithm.h library. You can use the tolower function from the cctype library:
#include <cctype>

int count_upper(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i