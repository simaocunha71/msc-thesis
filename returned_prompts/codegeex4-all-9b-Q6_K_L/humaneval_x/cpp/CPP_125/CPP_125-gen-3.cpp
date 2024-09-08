```cpp
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> split_words(string txt) {
    vector<string> res;
    string word;
    int n = txt.size();
    for (int i = 0; i < n; ++i) {
        if (txt[i] == ' ') {
            if (!word.empty()) {
                res.push_back(word);
                word.clear();
            }
        } else if (txt[i] == ',') {
            if (!word.empty()) {
                res.push_back(word);
                word.clear();
            }
            res.push_back(",");
        } else {
            word += txt[i];
        }
    }
    if (!word.empty()) {
        res.push_back(word);
    }
    if (res.empty()) {
        int count = 0;
        for (char c : txt) {
            if (islower(c) && (c - 'a') % 2 != 0) {
                ++count;
            }
        }
        res.push_back(to_string(count));
    }
    return res;
}
```