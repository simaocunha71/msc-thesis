```cpp
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> split_words(string txt) {
    vector<string> res;
    string temp = "";
    bool isComma = false;
    for (char c : txt) {
        if (c == ' ') {
            if (temp.length() > 0) {
                res.push_back(temp);
                temp = "";
            }
        } else if (c == ',') {
            if (temp.length() > 0) {
                res.push_back(temp);
                temp = "";
            }
            isComma = true;
        } else {
            temp += c;
        }
    }
    if (temp.length() > 0) {
        res.push_back(temp);
    }
    if (res.empty()) {
        int count = 0;
        for (char c : txt) {
            if (c >= 'a' && c <= 'z' && (c - 'a') % 2 != 0) {
                count++;
            }
        }
        res.push_back(to_string(count));
    }
    return res;
}
```