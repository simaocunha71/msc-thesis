
has_close_elements
I have a few suggestions for this function:

Use the standard library function next_permutation to generate all possible pairs of indices.  This is more efficient than a nested loop over indices.
Use the standard library function min_element to find the minimum element in the array, and calculate the difference between this element and the maximum element.
This function could be implemented as a member function of the vector class, or as a free function taking a vector and its size.  I'd prefer the latter, as it would allow the function to be used with other containers.
The function takes a vector of floats, but the return value is a bool.  This is confusing, as it suggests the function is working with floating-point numbers.  A better approach would be to return the index of the pair of numbers that are closest together, or -1 if no such pair exists.

Here's an example implementation:
#include <algorithm>
#include <vector>

bool has_close_elements(const std::vector<float>& numbers, float threshold) {
    if (numbers.size() < 2) {
        return false;
    }

    float min = *std::min_element(numbers.begin(), numbers.end());
    float max = *std::max_element(numbers.begin(), numbers.end());

    return max - min < threshold;
}

separate_paren_groups
This function has a bug.  If the input string contains spaces, the function will not correctly separate the parentheses groups.  You should remove the spaces before processing the string.
Also, it's a good idea to check that the input string is balanced before attempting to separate the groups.  You can do this by maintaining a balance counter as you iterate over the string.

Here's an example implementation:
#include <algorithm>
#include <string>
#include <vector>

std::vector<std::string> separate_paren_groups(const std::string& paren_string) {
    std::vector<std::string> all_parens;
    std::string current_paren;
    int level = 0;
    for (char chr : paren_string) {
        if (chr == '(') {
            level++;
        } else if