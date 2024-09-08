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
#include<ctype.h>
#include<string>
#include<algorithm>
using namespace std;
string get_closest_vowel(string word){
    for (int i=word.length()-1;i>=2;i--){
        char ch=word[i];
        if (isalpha(ch)){
            if (isalpha(word[i-1])&&isalpha(word[i-2])){
                if (word[i-1]!='a'&&word[i-1]!='e'&&word[i-1]!='i'&&word[i-1]!='o'&&word[i-1]!='u'&&word[i-1]!='A'&&word[i-1]!='E'&&word[i-1]!='I'&&word[i-1]!='O'&&word[i-1]!='U'){
                    if (word[i-2]!='a'&&word[i-2]!='e'&&word[i-2]!='i'&&word[i-2]!='o'&&word[i-2]!='u'&&word[i-2]!='A'&&word[i-2]!='E'&&word[i-2]!='I'&&word[i-2]!='O'&&word[i-2]!='U'){
                        if ((word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'||word[i]=='A'||word[i]=='E'||word[i]=='I'||word[i]=='O'||word[i]=='U')){
                            return string(1,word[i]);
                        }
                    }
                }
            }
        }
    }
    return "";
}
int main(){
    string s1="yogurt";
    string s2="FULL";
    string s3="quick";
    string s4="ab";
    string s5="y";
    string s6="FULL";
    string s7="quick";
    string s8="a";
    string s9="FULL";
    string s10="quick";
    string s11="ab";
    printf("%s\n",get_close