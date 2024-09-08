#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

vector<string> words_string(string s) {
    vector<string> words;
    string word;
    for (char c : s) {
        if (c == ',') {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else if (c != ' ') {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }
    return words;
}

C:
#include <cctype>
#include <string>
#include <vector>
using namespace std;

vector<string> words_string(string s) {
    vector<string> words;
    string word;
    for (char c : s) {
        if (isspace(c)) {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }
    return words;
}

D:
#include <cctype>
#include <string>
#include <vector>
using namespace std;

vector<string> words_string(string s) {
    vector<string> words;
    string word;
    for (char c : s) {
        if (isspace(c)) {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }
    return words;
}

E:
#include <cctype>
#include <string>
#include <vector>
using namespace std;

vector<string> words_string(string s) {
    vector<string> words;
    string word;
    for (char c : s) {
        if (isspace(c)) {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += c;
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }
    return words;
}

F:
#include <cctype>
#include <string>
#include <vector>
using namespace std;

vector<string> words_string(string s) {
    vector<string> words;
    string word;
    for (char c : s) {
        if (isspace(c)) {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word