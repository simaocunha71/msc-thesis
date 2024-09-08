    vector<string> result;
    size_t start = 0;
    size_t end = txt.find(' ');
    while (end != string::npos) {
        result.push_back(txt.substr(start, end - start));
        start = end + 1;
        end = txt.find(' ', start);
    }
    if (end == string::npos) {
        result.push_back(txt.substr(start));
    }
    else {
        result.push_back(txt.substr(start, end - start));
    }

    // if no whitespaces exists in the text
    if (result.size() == 1) {
        string temp;
        for (char c : txt) {
            if (isalpha(c)) {
                temp += c;
            }
        }
        int count = 0;
        for (char c : temp) {
            if ((int)(c - 'a') % 2 != 0) {
                count++;
            }
        }
        result.push_back(to_string(count));
    }
    return result;
}

int main() {
    printf("%s\n", split_words("Hello world!")[0].c_str());
    printf("%s\n", split_words("Hello,world!")[0].c_str());
    printf("%s\n", split_words("abcdef")[0].c_str());
    return 0;
}

B:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;
    string temp = "";

    // Split by whitespace
    for (char c : txt) {
        if (c == ' ') {
            if (!temp.empty()) {
                result.push_back(temp);
                temp = "";
            }
        } else if (c == ',') {
            if (!temp.empty()) {
                result.push_back(temp);
                temp = "";
            }
        } else {
            temp += c;
        }
    }

    // Add the last word
    if (!temp.empty()) {
        result.push_back(temp);
    }

    // If no words were found, count the odd letters
    if (result.size() == 0) {
        int count = 0;
        for (char c : txt) {
            if (isalpha(c) && (int)(c - 'a') % 2 != 0) {
                count++;
            }
        }
        result.push_back(to_string(count));
    }

    return result;
}

int main() {
    cout