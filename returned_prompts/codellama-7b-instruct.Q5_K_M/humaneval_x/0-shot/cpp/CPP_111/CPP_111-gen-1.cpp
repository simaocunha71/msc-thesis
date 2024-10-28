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
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    map<char,int> temp;
    string word;
    map<char,int> final;
    int count=0;
    int max = 0;
    int i=0;
    int j=0;
    while(i<test.length()){
        word="";
        while(test[i]!=' '&&i<test.length()){
            word+=test[i];
            i++;
        }
        i++;
        for(j=0;j<word.length();j++){
            if(temp.find(word[j])!=temp.end()){
                temp[word[j]]++;
            }
            else{
                temp[word[j]]=1;
            }
        }
    }
    for(map<char,int>::iterator it = temp.begin();it!=temp.end();it++){
        if(it->second>max){
            max = it->second;
            final.insert(*it);
        }
        else if(it->second==max){
            final.insert(*it);
        }
    }
    return final;
}



















































