```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;
    string current_word;

    for (char c : txt) {
        if (isspace(c) || c == ',') {
            if (!current_word.empty()) {
                result.push_back(current_word);
                current_word.clear();
            }
            if (c == ',') {
                result.push_back(",");
            }
        } else {
            current_word.push_back(c);
        }
    }

    if (!current_word.empty()) {
        result.push_back(current_word);
    }

    if (result.empty()) {
        int count = 0;
        for (char c : txt) {
            if (islower(c) && c - 'a' % 2 != 0) {
                count++;
            }
        }
        result.push_back(to_string(count));
    }

    return result;
}
```