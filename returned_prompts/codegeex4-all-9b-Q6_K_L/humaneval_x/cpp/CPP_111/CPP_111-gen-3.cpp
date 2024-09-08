#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
    int max = 0;
    map<char,int> res;
    map<char,int> count;
    for(int i = 0; i < test.length(); i++){
        count[test[i]]++;
    }
    for(char c: count){
        if(count[c] > max){
            max = count[c];
            res.clear();
            res[c] = max;
        } else if(count[c] == max){
            res[c] = max;
        }
    }
    return res;
} 
