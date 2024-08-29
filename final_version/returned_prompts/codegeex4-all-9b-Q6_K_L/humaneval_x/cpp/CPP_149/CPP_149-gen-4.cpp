#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool sortStrings(string a, string b) {
    if (a.size() == b.size())
        return a < b;
    return a.size() < b.size();
}

vector<string> vector_sort(vector<string>& words) {
    // Remove the words with odd length
    words.erase(remove_if(words.begin(), words.end(), [](const string& word) {
        return word.size() % 2 != 0;
    }), words.end());

    // Sort the words
    sort(words.begin(), words.end(), sortStrings);

    return words;
}

int main() {
    vector<string> words = {"aa", "a", "aaa"};
    vector<string> result = vector_sort(words);

    for (const string& word : result) {
        cout << word << " ";
    }
    cout << endl;

    return 0;
}