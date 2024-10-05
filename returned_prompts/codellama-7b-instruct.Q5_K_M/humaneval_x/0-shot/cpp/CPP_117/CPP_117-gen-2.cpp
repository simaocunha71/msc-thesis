/*
Given a string s and a natural number n, you have been tasked to implement 
a function that returns a vector of all words from string s that contain exactly 
n consonants, in order these words appear in the string s.
If the string s is empty then the function should return an empty vector.
Note: you may assume the input string contains only letters and spaces.
Examples:
select_words("Mary had a little lamb", 4) ==> {"little"}
select_words("Mary had a little lamb", 3) ==> {"Mary", "lamb"}
select_words('simple white space", 2) ==> {}
select_words("Hello world", 4) ==> {"world"}
select_words("Uncle sam", 3) ==> {"Uncle"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> v;
    if (s.empty()) return v;
    string word;
    for (auto c : s) {
        if (c == ' ') {
            if (word.size() == n) v.push_back(word);
            word.clear();
        } else {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') continue;
            word += c;
        }
    }
    if (word.size() == n) v.push_back(word);
    return v;
}

