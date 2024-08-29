```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> split_words(string txt) {
    vector<string> res;
    if (txt.find(' ') != string::npos) {
        res = split(txt, ' ');
    } else if (txt.find(',') != string::npos) {
        res = split(txt, ',');
    } else {
        int count = 0;
        for (char c : txt) {
            if (islower(c) && (c - 'a') % 2 == 1) {
                count++;
            }
        }
        res.push_back(to_string(count));
    }
    return res;
}

vector<string> split(string txt, char delimiter) {
    vector<string> res;
    string word = "";
    for (char c : txt) {
        if (c == delimiter) {
            res.push_back(word);
            word = "";
        } else {
            word += c;
        }
    }
    res.push_back(word);
    return res;
}

int main() {
    vector<string> res = split_words("Hello world!");
    for (string word : res) {
        cout << word << " ";
    }
    cout << endl;
    res = split_words("Hello,world!");
    for (string word : res) {
        cout << word << " ";
    }
    cout << endl;
    res = split_words("abcdef");
    for (string word : res) {
        cout << word << " ";
    }
    cout << endl;
    return 0;
}
```