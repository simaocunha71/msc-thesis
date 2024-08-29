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

    string vowels = "aeiouAEIOU";
    string consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    string result = "";
    for(int i=0;i<word.length();i++){
        if(vowels.find(word[i])!=string::npos){
            int j = i+1;
            while(j<word.length() && consonants.find(word[j])!=string::npos){
                j++;
            }
            if(j<word.length()){
                int k = j+1;
                while(k<word.length() && consonants.find(word[k])!=string::npos){
                    k++;
                }
                if(k<word.length()){
                    result = word[j];
                    break;
                }
            }
        }
    }
    return result;
}

int main(){
    string word;
    printf("Enter a word: ");
    cin>>word;
    string result = get_closest_vowel(word);
    if(result==""){
        printf("No vowel found between two consonants from the right side of the word.\n");
    }
    else{
        printf("The closest vowel that stands between two consonants from the right side of the word is: %s\n",result.c_str());
    }
    return 0;
}
