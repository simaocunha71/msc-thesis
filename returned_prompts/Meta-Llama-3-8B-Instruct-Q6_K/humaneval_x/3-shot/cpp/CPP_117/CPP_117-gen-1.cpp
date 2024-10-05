    vector<string> result;
    string word;
    int count=0;
    for (int i=0;i<s.length();i++)
    {
        if (isalnum(s[i]))
        {
            word+=s[i];
            if (!isalpha(s[i])) continue;
            if (s[i]=='y') continue;
            if (s[i]=='w') continue;
            count+=1;
        }
        else
        {
            if (count==n)
            {
                result.push_back(word);
                word="";
                count=0;
            }
            else
            {
                word="";
                count=0;
            }
        }
    }
    if (count==n)
    {
        result.push_back(word);
    }
    sort(result.begin(),result.end());
    return result;
}  // 1st approach
// 2nd approach:
#include <cctype>
using namespace std;
vector<string> select_words(string s, int n) {
    vector<string> result;
    string word;
    int count = 0;
    for (char c : s) {
        if (isalnum(c)) {
            word += c;
            if (!isalpha(c)) continue;
            if (c == 'y' || c == 'w') continue;
            if (isalpha(c)) count++;
        } else {
            if (count == n) {
                result.push_back(word);
                word.clear();
                count = 0;
            } else {
                word.clear();
                count = 0;
            }
        }
    }
    if (count == n) {
        result.push_back(word);
    }
    sort(result.begin(), result.end());
    return result;
}  // 3rd approach:
#include <cctype>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
vector<string> select_words(string s, int n) {
    vector<string> result;
    vector<string> words;
    string word;
    for (char c : s) {
        if (isalnum(c)) {
            word += c;
        } else {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        }
    }
    if (!word.empty()) {
        words.push_back(word);
    }
    for (string& w : words) {
        int count = 0;
        for (char c : w) {
            if (!isalpha(c) || c == 'y' || c == 'w')