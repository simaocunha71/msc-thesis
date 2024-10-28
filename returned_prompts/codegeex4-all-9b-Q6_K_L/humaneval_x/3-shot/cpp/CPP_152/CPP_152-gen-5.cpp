
A couple of comments on your code:

Don't use using namespace std. It's a bad habit that can lead to name clashes.
The for loops in your functions have the same name (i), which is confusing.
You don't need to do level-=1 when you find a closing parenthesis. You can just break out of the for loop.

Here is a refactored version of your code:

#include <vector>
#include <cmath>
#include <string>

std::vector<float> has_close_elements(const std::vector<float>& numbers, float threshold) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (std::abs(numbers[i] - numbers[j]) < threshold) {
                return {true};
            }
        }
    }
    return {false};
}

std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
        }
        current_paren += chr;
        if (chr == ')') {
            --level;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren.clear();
            }
        }
    }
    return all_parens;
}

float truncate_number(float number) {
    return number - static_cast<int>(number);
}

std::vector<int> compare(const std::vector<int>& game, const std::vector<int>& guess) {
    std::vector<int> all_scores;
    for (size_t i = 0; i < game.size(); ++i) {
        all_scores.push_back(std::abs(game[i] - guess[i]));
    }
    return all_scores;
}

Note that I've changed the return types of your functions to use the standard library containers and types. This is a good habit to get into, as it makes your code more portable and easier to read.