
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    return adjacent_find(numbers.begin(), numbers.end(), [threshold](float a, float b) {
        return abs(a - b) < threshold;
    }) != numbers.end();
}

vector<string> separate_paren_groups(string paren_string) {
    vector<string> result;
    string current;
    int level = 0;
    for (char c : paren_string) {
        if (c == '(') {
            ++level;
        } else if (c == ')') {
            --level;
        }
        current += c;
        if (level == 0) {
            result.push_back(current);
            current.clear();
        }
    }
    return result;
}

float truncate_number(float number) {
    return number - floor(number);
}

string Strongest_Extension(string class_name, vector<string> extensions) {
    auto cmp = [](const string& a, const string& b) {
        int strength_a = 0, strength_b = 0;
        for (char c : a) {
            strength_a += isupper(c) ? 1 : -1;
        }
        for (char c : b) {
            strength_b += isupper(c) ? 1 : -1;
        }
        return strength_a < strength_b;
    };
    auto it = max_element(extensions.begin(), extensions.end(), cmp);
    return class_name + '.' + *it;
}

#include <cassert>

int main() {
    assert(!has_close_elements({1.0, 2.0, 3.0}, 0.5));
    assert(has_close_elements({1.0, 2.8, 3.0, 4.0,