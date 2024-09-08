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
#include<map>
#include<string>
using namespace std;
map<char,int> histogram(string test){
    int max = 0;
    map<char,int> letters;
    map<char,int>::iterator it;
    for(int i = 0; i < test.length(); i++){
        if(letters.find(test[i]) == letters.end()){
            letters[test[i]] = 1;
        }
        else{
            letters[test[i]]++;
        }
    }
    for(it = letters.begin(); it!=letters.end(); it++){
        if(it->second > max){
            max = it->second;
        }
    }
    for(it = letters.begin(); it!=letters.end(); it++){
        if(it->second == max){
            printf("%c:%d", it->first, it->second);
        }
    }
    return letters;
}
B:
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
#include<map>
#include<string>
using namespace std;
map<char,int> histogram(string test){
    int max = 0;
    map<char,int> letters;
    map<char,int>::iterator it;
    for(int i = 0; i < test.length(); i