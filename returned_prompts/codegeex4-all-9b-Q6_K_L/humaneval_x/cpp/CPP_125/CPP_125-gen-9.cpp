```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;
    string current_word = "";
    bool has_space = false;
    bool has_comma = false;
    int odd_count = 0;

    for (char c : txt) {
        if (isspace(c)) {
            has_space = true;
            if (!current_word.empty()) {
                result.push_back(current_word);
                current_word = "";
            }
        } else if (c == ',') {
            has_comma = true;
            if (!current_word.empty()) {
                result.push_back(current_word);
                current_word = "";
            }
        } else if (islower(c)) {
            if ((c - 'a') % 2 != 0) {
                odd_count++;
            }
        }
        if (!has_space && !has_comma) {
            current_word += c;
        }
    }

    if (!current_word.empty()) {
        result.push_back(current_word);
    } else if (odd_count > 0) {
        result.push_back(to_string(odd_count));
    }

    return result;
}
```

Explanation:
1. Initialize an empty vector `result` to store the split words.
2. Initialize a string `current_word` to store the current word being processed.
3. Initialize boolean variables `has_space` and `has_comma` to track if a space or comma has been encountered.
4. Initialize an integer `odd_count` to count the number of lowercase letters with an odd order in the alphabet.
5. Iterate over each character `c` in the input string `txt`.
6. If `c` is a space, set `has_space` to true and check if `current_word` is not empty. If it is not empty, add it to `result` and reset `current_word` to an empty string.
7. If `c` is a comma, set `has_comma` to true and check if `current_word` is not empty. If it is not empty, add it to `result` and reset `current_word` to an empty string.
8. If `c` is a lowercase letter, check if its order in the alphabet is odd. If it is, increment `odd_count`.
9. If `has_space` and `has_comma` are both false, append `c` to `current_word`.
10. After the loop