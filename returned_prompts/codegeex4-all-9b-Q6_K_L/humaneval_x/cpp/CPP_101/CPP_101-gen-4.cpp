#include <string>
#include <vector>
#include <sstream>
using namespace std;

vector<string> words_string(string s) {
    stringstream ss(s);
    string word;
    vector<string> words;

    while (ss >> word) {
        words.push_back(word);
    }

    return words;
}
