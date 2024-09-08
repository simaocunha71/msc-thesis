```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> split_words(string txt) {
    // Check if there are any spaces in the text
    if (txt.find(" ") != string::npos) {
        // Split the text on spaces
        vector<string> result;
        string word;
        for (char c : txt) {
            if (c == ' ') {
                if (!word.empty()) {
                    result.push_back(word);
                    word.clear();
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            result.push_back(word);
        }
        return result;
    }

    // Check if there are any commas in the text
    if (txt.find(",") != string::npos) {
        // Split the text on commas
        vector<string> result;
        string word;
        for (char c : txt) {
            if (c == ',') {
                if (!word.empty()) {
                    result.push_back(word);
                    word.clear();
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            result.push_back(word);
        }
        return result;
    }

    // Count the number of lower-case letters with odd order in the alphabet
    int count = 0;
    for (char c : txt) {
        if (c >= 'a' && c <= 'z') {
            if ((c - 'a') % 2 != 0) {
                count++;
            }
        }
    }
    return {to_string(count)};
}

int main() {
    vector<string> result = split_words("abcdef");
    for (string word : result) {
        cout << word << endl;
    }
    return 0;
}
```