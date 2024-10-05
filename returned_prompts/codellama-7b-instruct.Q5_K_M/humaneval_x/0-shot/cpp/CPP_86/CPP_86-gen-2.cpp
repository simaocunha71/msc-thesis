/*
Write a function that takes a string and returns an ordered version of it.
Ordered version of string, is a string where all words (separated by space)
are replaced by a new word where all the characters arranged in
ascending order based on ascii value.
Note: You should keep the order of words and blank spaces in the sentence.

For example:
anti_shuffle("Hi") returns "Hi"
anti_shuffle("hello") returns "ehllo"
anti_shuffle("Hello World!!!") returns "Hello !!!Wdlor"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string new_string;
    string words[100];
    int i = 0;
    for(int j = 0; j < s.length(); j++){
        if(s[j] == ' '){
            words[i] = "";
            i++;
        }
        else{
            words[i] += s[j];
        }
    }
    for(int k = 0; k < i; k++){
        sort(words[k].begin(), words[k].end());
        new_string += words[k];
    }
    return new_string;
}

