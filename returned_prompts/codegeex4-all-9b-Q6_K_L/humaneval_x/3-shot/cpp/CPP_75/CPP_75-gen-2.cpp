
Your code is not formatted correctly, it looks like it's being cut off or something. There's also some unnecessary whitespace before the comment blocks. You also seem to be mixing tabs and spaces in your code, which can make it difficult to read. You should stick to one or the other.
Also, you're using using namespace std; in your code, which is generally considered bad practice. It's better to prefix your standard library names with std::.
I'm also going to assume that you're using C++11 or later, since you're using auto and the range-based for loop.
Here's some code with some minor changes:

#include <algorithm>
#include <cmath>
#include <vector>

using std::abs;
using std::auto;
using std::max;
using std::min;
using std::sort;
using std::vector;

bool has_close_elements(vector<float> numbers, float threshold) {
    sort(numbers.begin(), numbers.end());
    for (auto i = 1u; i < numbers.size(); ++i) {
        if (numbers[i] - numbers[i - 1] < threshold) {
            return true;
        }
    }
    return false;
}

vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (auto chr : paren_string) {
        if (chr == '(') {
            ++level;
        } else if (chr == ')') {
            --level;
        }
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }
    return all_parens;
}

float truncate_number(float number) {
    return number - static_cast<float>(static_cast<int>(number));
}

bool is_multiply_prime(int a) {
    vector<int> primes;
    for (int i = 2; i < 100; ++i) {
        if (primes.empty() || primes.back() != i) {
            primes.push_back(i);
