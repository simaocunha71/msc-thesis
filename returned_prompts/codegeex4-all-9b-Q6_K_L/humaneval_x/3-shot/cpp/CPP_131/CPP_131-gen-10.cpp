
has_close_elements

You don't need two loops.  You can just increment j by 1 in the for loop.  And you don't need to use abs.  The subtraction is already positive.
for (j = i + 1; j < numbers.size(); ++j) {
    if (numbers[i] - numbers[j] < threshold) {
        return true;
    }
}

separate_paren_groups

This function works, but it's not very robust.  There are lots of edge cases that it doesn't handle.  For example, it will fail with a string that has a parenthesis that is not properly closed.  To make it more robust, you should check that the level is zero after you've finished iterating through the string.
Also, you can use the stringstream class to make this easier.  Here's an example:
#include <sstream>

std::vector<std::string> separate_paren_groups(std::string paren_string) {
    std::vector<std::string> all_parens;
    std::stringstream ss(paren_string);
    std::string current_paren;
    std::string temp;
    int level = 0;

    while (std::getline(ss, temp, '(')) {
        current_paren += temp;
        while (true) {
            if (std::getline(ss, temp, ')')) {
                current_paren += temp;
                if (++level == 0) {
                    all_parens.push_back(current_paren);
                    current_paren = "";
                    break;
                }
            }
        }
    }

    return all_parens;
}

truncate_number

You don't need the int() cast.  You can use the fmod() function from the math.h library to get the decimal part of the number.
float truncate_number(float number) {
    return fmod(number, 1.0f);
}

digits

This function works, but it's not very efficient.  You can use the % operator to get the last digit of the number, and then use the / operator to remove the last digit from the number.
