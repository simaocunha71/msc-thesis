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
#include<string>
#include<algorithm>
using namespace std;
string get_closest_vowel(string word){
    string vowels="aeiouAEIOU";
    string consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    string result="";
    int i=word.size()-1;
    while(i>=0){
        if(vowels.find(word[i])==string::npos){
            if(consonants.find(word[i-1])!=string::npos && vowels.find(word[i-2])!=string::npos){
                result=word[i-2];
                break;
            }
            i--;
        }else{
            i--;
        }
    }
    return result;
}