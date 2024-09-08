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

    map<char,int> m;
    map<char,int>::iterator it;
    int max=0;
    int count=0;

    for(int i=0;i<test.size();i++){
        it=m.find(test[i]);
        if(it!=m.end()){
            count=it->second+1;
            m.erase(it);
            m.insert(make_pair(test[i],count));
        }
        else{
            m.insert(make_pair(test[i],1));
        }
    }

    for(it=m.begin();it!=m.end();it++){
        if(it->second>max){
            max=it->second;
        }
    }

    map<char,int> result;
    for(it=m.begin();it!=m.end();it++){
        if(it->second==max){
            result.insert(make_pair(it->first,it->second));
        }
    }
    return result;
}
