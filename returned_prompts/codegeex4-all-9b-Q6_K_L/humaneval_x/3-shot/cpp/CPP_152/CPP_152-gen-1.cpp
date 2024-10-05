
First, here are some things that may be of interest to you.
1. Use of using namespace std
Using using namespace std is generally not recommended as it can lead to name collisions. It is better to prefix the standard library names with std::. For example, instead of writing vector<int>, write std::vector<int>. This is not a problem in your current code, but it is a good practice to follow.
2. Using std::abs
Instead of writing abs(numbers[i]-numbers[j]), write std::abs(numbers[i]-numbers[j]). This is because abs is a macro that can lead to unexpected behavior. For example, if numbers[i] and numbers[j] are large enough, abs(numbers[i]-numbers[j]) may overflow. To avoid this, use std::abs.
3. Using std::string::push_back
Instead of writing current_paren+=chr, write current_paren.push_back(chr). This is because the += operator is not defined for std::string.
4. Using std::vector::push_back
Instead of writing all_parens.push_back(current_paren), write all_parens.push_back(std::move(current_paren)). This is because the push_back method has a copy constructor that makes a copy of the current_paren string. If you want to move the contents of current_paren into all_parens, use std::move to avoid a copy.
5. Using std::round
Instead of writing number-int(number), write std::round(number-int(number)). This is because the floating-point division operator / may result in a loss of precision. To avoid this, use std::round to round the result to the nearest integer.
6. Using std::abs
Instead of writing abs(game[i]-guess[i]), write std::abs(game[i]-guess[i]). This is because the abs macro is not defined for std::vector.
7. Using std::move
Instead of writing result.push_back(abs(game[i]-guess[i])), write result.push_back(std::move(abs(game[i]-guess[i]))). This is because the push_back method has a copy constructor that makes