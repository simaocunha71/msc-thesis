#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string fix_spaces(string text) {
    stringstream ss;
    bool space_count = false;
    for (char c: text) {
        if (c == ' ') {
            space_count = true;
        }
        else {
            if (space_count) {
                ss << '-';
            }
            space_count = false;
            ss << c;
        }
    }
    if (space_count) {
        ss << '-';
    }
    return ss.str();
}

int main() {
    cout << fix_spaces("Example") << endl; // "Example"
    cout << fix_spaces("Example 1") << endl; // "Example_1"
    cout << fix_spaces(" Example 2") << endl; // "_Example_2"
    cout << fix_spaces(" Example   3") << endl; // "_Example-3"
    return 0;
}