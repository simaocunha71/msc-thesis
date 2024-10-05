/*
Given a string of words, return a vector of words split on whitespace, if no whitespaces exists in the text you
should split on commas ',' if no commas exists you should return a vector with one element, the number of lower-case letters with odd order in the
alphabet, ord("a") = 0, ord("b") = 1, ... ord("z") = 25
Examples
split_words("Hello world!") ➞ {"Hello", "world!"}
split_words("Hello,world!") ➞ {"Hello", "world!"}
split_words("abcdef") == {"3"} 
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> split_words(string txt){
    vector<string> words;
    string word;
    for(int i=0;i<txt.size();i++){
        if(txt[i]==' '||txt[i]==','){
            if(word!=""){
                words.push_back(word);
                word="";
            }
        }
        else{
            word+=txt[i];
        }
    }
    if(word!="")
        words.push_back(word);
    return words;
}
