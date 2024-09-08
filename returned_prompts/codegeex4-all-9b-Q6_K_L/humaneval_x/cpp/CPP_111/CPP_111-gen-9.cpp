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
    map<char,int> hist;
    string temp;
    for(int i=0;i<test.size();i++){
        if(test[i]==' '){
            hist[temp[0]]++;
            temp.clear();
        }
        else{
            temp.push_back(test[i]);
        }
    }
    hist[temp[0]]++;
    map<char,int>::iterator it;
    map<int,vector<char>> reverseHist;
    for(it=hist.begin();it!=hist.end();it++){
        reverseHist[it->second].push_back(it->first);
    }
    int max=0;
    for(map<int,vector<char>>::iterator i=reverseHist.begin();i!=reverseHist.end();i++){
        if(i->first>max){
            max=i->first;
        }
    }
    map<char,int> result;
    for(map<int,vector<char>>::iterator i=reverseHist.begin();i!=reverseHist.end();i++){
        if(i->first==max){
            for(int j=0;j<i->second.size();j++){
                result[i->second[j]]=max;
            }
        }
    }
    return result;
}
