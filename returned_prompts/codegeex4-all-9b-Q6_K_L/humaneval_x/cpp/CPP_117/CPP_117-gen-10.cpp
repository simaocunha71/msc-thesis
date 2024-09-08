#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool isConsonant(char c) {
    c = tolower(c);
    return (c >= 'b' && c <= 'z') && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}
vector<string> select_words(string s,int n){
    vector<string> res;
    string word = "";
    int consonants = 0;
    for (char c : s) {
        if (c == ' ') {
            if (!word.empty() && consonants == n) {
                res.push_back(word);
            }
            word = "";
            consonants = 0;
        } else {
            if (isConsonant(c)) {
                consonants++;
            }
            word += c;
        }
    }
    if (!word.empty() && consonants == n) {
        res.push_back(word);
    }
    return res;
}
int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for (string word : words) {
        printf("%s\n", word.c_str());
    }
    return 0;
}

C:
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
bool is_consonant(char c) {
    c = tolower(c);
    return (c >= 'b' && c <= 'z') && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}
vector<string> select_words(string s, int n) {
    vector<string> res;
    string word = "";
    int consonants = 0;
    for (char c : s) {
        if (c == ' ') {
            if (!word.empty() && consonants == n) {
                res.push_back(word);
            }
            word = "";
            consonants = 0;
        } else {
            if (is_consonant(c)) {
                consonants++;
            }
            word += c;
        }
    }
    if (!word.empty() && consonants == n) {
        res.push_back(word);
    }
    return res;
}
int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for (string word : words) {
        printf("%s\n", word.c_str());
