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
	int index=0, i=0, j=1, close=1;
	while(j<=word.length())
    {
        if(!isalpha(word[i])){break;}
        else{if((close==-1)||(index>i-3&&i<close))
            {
                index++;
                j=i+2;
            }
            else{
                close=i; break;}}
        i++;}
    return word.substr(0, index);
    
}