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
    string max_word = "";
    int max_unique_chars = 0;
    for(int i = 0; i < words.size(); i++){
        string word = words[i];
        sort(word.begin(), word.end());
        word.erase(unique(word.begin(), word.end()), word.end());
        if(word.length() > max_unique_chars){
            max_unique_chars = word.length();
            max_word = words[i];
        }
        else if(word.length() == max_unique_chars){
            if(words[i] < max_word){
                max_word = words[i];
            }
        }
    }
    return max_word;
}
