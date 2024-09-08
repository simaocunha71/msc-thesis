/*
Write a function that accepts a vector of strings.
The vector contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max({"name", "of", 'string'}) == 'string"
find_max({"name", "enam", "game"}) == "enam"
find_max({"aaaaaaa", "bb" ,"cc"}) == "aaaaaaa"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){

    int max_unique_char = 0;
    string max_unique_word = "";
    for (int i = 0; i < words.size(); i++) {
        int unique_char_count = 0;
        vector<char> unique_chars;
        for (int j = 0; j < words[i].size(); j++) {
            bool is_unique = true;
            for (int k = 0; k < unique_chars.size(); k++) {
                if (unique_chars[k] == words[i][j]) {
                    is_unique = false;
                    break;
                }
            }
            if (is_unique) {
                unique_chars.push_back(words[i][j]);
                unique_char_count++;
            }
        }
        if (unique_char_count > max_unique_char) {
            max_unique_char = unique_char_count;
            max_unique_word = words[i];
        } else if (unique_char_count == max_unique_char) {
            if (words[i] < max_unique_word) {
                max_unique_word = words[i];
            }
        }
    }
    return max_unique_word;
}

int main() {
    vector<string> words = {"name", "of", "string"};
    string max_unique_word = find_max(words);
    printf("The word with maximum number of unique characters is: %s\n", max_unique_word.c_str());
    return 0;
}

