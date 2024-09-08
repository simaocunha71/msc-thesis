/*
Given a string representing a space separated lowercase letters, return a map
of the letter with the most repetition and containing the corresponding count.
If several letters have the same occurrence, return all of them.

Example:
histogram("a b c") == {{"a", 1}, {"b", 1}, {"c", 1}}
histogram("a b b a") == {{"a", 2}, {"b", 2}}
histogram("a b c a b") == {{"a", 2}, {"b", 2}}
histogram("b b b b a") == {{"b", 4}}
histogram("") == {}

*/
#include<stdio.h>
#include<map>
#include<string>
#include<vector>
using namespace std;
map<char,int> histogram(string test){
    map<char,int> hist;
    int max = 0;
    char most_frequent;
    string s;
    int len = test.length();
    for (int i = 0; i < len; i++) {
        if (test[i] == ' ') {
            if (hist[s[0]] > max) {
                hist[s[0]] = max;
                most_frequent = s[0];
            }
            else if (hist[s[0]] == max) {
                hist[s[0]] = max;
                most_frequent = s[0];
            }
            s = "";
        }
        else {
            s += test[i];
        }
    }
    map<char,int>::iterator it;
    for (it = hist.begin(); it != hist.end(); it++) {
        if (it->second == max) {
            cout<<it->first<<" "<<it->second<<endl;
        }
    }
    map<char,int> result;
    result[most_frequent] = max;
    return result;
}

B:
/*
Given a string representing a space separated lowercase letters, return a map
of the letter with the most repetition and containing the corresponding count.
If several letters have the same occurrence, return all of them.

Example:
histogram("a b c") == {{"a", 1}, {"b", 1}, {"c", 1}}
histogram("a b b a") == {{"a", 2}, {"b", 2}}
histogram("a b c a b") == {{"a", 2}, {"b", 2}}
histogram("b b b b a") == {{"b", 4