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
    string vowels="AEIOUaeiou";
    string ans="";
    for(int i=word.length()-1;i>=1;i--){
        if(vowels.find(word[i])!=-1 && vowels.find(word[i-1])==-1 && vowels.find(word[i+1])==-1){
            ans+=word[i];
            break;
        }
    }
    return ans;

}
int main(){
    string word;
    cin>>word;
    cout<<get_closest_vowel(word)<<endl;
    return 0;
}