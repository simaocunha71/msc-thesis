
I'll focus on the third problem, since it's the only one I've actually seen.  I'll also assume you're using C++11 or later, since your code uses auto.
First of all, your map is not necessary.  C++11 provides the string_view type, which is a non-owning, constant view into a string.  This can be used to create a map from strings to integers, with the string_view as the key.
Second, you should use the standard library sort function.  This function is a template function, and can be used to sort any container, including a vector of string_views.  You can use the lambda function [=](const string_view& lhs, const string_view& rhs) { return digit_to_int[lhs] < digit_to_int[rhs]; } to specify how the strings are sorted.
Finally, the sort function sorts the container in place, so you don't need to return anything.  The original vector will be sorted.
Here's a complete solution:
#include <algorithm>
#include <string>
#include <string_view>
#include <vector>

std::vector<std::string_view> digit_to_int = {
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
};

std::vector<std::string_view> sort_numbers(std::