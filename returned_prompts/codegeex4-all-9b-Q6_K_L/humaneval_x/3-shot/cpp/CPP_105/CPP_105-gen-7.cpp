
has_close_elements
This function is fine. It's not very efficient though. For each pair of elements, it checks whether the difference is less than the threshold. There are n elements, so there are n(n-1)/2 pairs of elements. This function does n(n-1)/2 comparisons, which is O(n^2). A more efficient function would do n log n comparisons.
Here's the code with some minor improvements:

#include <cmath>
#include <vector>

using namespace std;

bool has_close_elements(const vector<float>& numbers, float threshold) {
    for (size_t i = 0; i < numbers.size(); ++i) {
        for (size_t j = i + 1; j < numbers.size(); ++j) {
            if (fabs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
This function is fine. It's not very efficient though. It loops through each character in the string, and for each character, it checks whether it's an opening or closing parenthesis. This means that it does n comparisons, where n is the length of the string. A more efficient function would do something like n log n comparisons.
Here's the code with some minor improvements:

#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    size_t i = 0;

    while (i < paren_string.length()) {
        char chr = paren_string[i];

        if (chr == '(') {
            level += 1;
            current_p