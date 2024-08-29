#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> select_words(string s, int n) {
    vector<string> result;
    string word;
    int consonant_count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            if (consonant_count == n) {
                result.push_back(word);
            }
            word = "";
            consonant_count = 0;
        } else {
            char c = tolower(s[i]);
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                consonant_count++;
            }
            word += s[i];
        }
    }
    if (consonant_count == n) {
        result.push_back(word);
    }
    return result;
}

int main() {
    vector<string> result = select_words("Mary had a little lamb", 4);
    for (string word : result) {
        cout << word << endl;
    }
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> select_words(string s, int n) {
    vector<string> result;
    string word;
    int consonant_count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            if (consonant_count == n) {
                result.push_back(word);
            }
            word = "";
            consonant_count = 0;
        } else {
            char c = tolower(s[i]);
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                consonant_count++;
            }
            word += s[i];
        }
    }
    if (consonant_count == n) {
        result.push_back(word);
    }
    return result;
}

int main() {
    vector<string> result = select_words("Mary had a little lamb", 4);
    for (string word : result) {
        cout << word << endl;
    }
    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> select