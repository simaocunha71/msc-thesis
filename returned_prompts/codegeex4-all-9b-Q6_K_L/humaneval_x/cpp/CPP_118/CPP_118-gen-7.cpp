/*
You are given a word. Your task is to find the closest vowel that stands between 
two consonants from the right side of the word (case sensitive).

Vowels in the beginning and ending doesn't count. Return empty string if you didn't
find any vowel met the above condition. 

You may assume that the given string contains English letter only.

Example:
get_closest_vowel("yogurt") ==> "u"
get_closest_vowel("FULL") ==> "U"
get_closest_vowel("quick") ==> ""
get_closest_vowel("ab") ==> ""
*/
#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
string get_closest_vowel(string word){
    int len = word.length();
    string vowels = "aeiou";
    string ans;
    for(int i = len - 1; i > 0; i--){
        char c = word[i];
        char prev = word[i-1];
        if(vowels.find(c) != string::npos && vowels.find(prev) != string::npos){
            ans = c;
            break;
        }
    }
    return ans;
}
