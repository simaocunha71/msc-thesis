#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<string> split_words(string txt){
    vector<string> words;
    string word = "";
    for (int i = 0; i < txt.size(); i++) {
        if (txt[i] == ' ' || txt[i] == ',') {
            if (word != "") {
                words.push_back(word);
                word = "";
            }
        } else {
            word += txt[i];
        }
    }
    if (word != "") {
        words.push_back(word);
    }
    if (words.size() == 0) {
        int odd_count = 0;
        for (int i = 0; i < txt.size(); i++) {
            if (txt[i] >= 'a' && txt[i] <= 'z') {
                if ((txt[i] - 'a') % 2 == 1) {
                    odd_count++;
                }
            }
        }
        words.push_back(to_string(odd_count));
    }
    return words;
}

int main() {
    vector<string> words = split_words("abcdef");
    for (string word : words) {
        cout << word << " ";
    }
    cout << endl;
    return 0;
}
