
#include<iostream>
#include<map>
#include<string>
using namespace std;

map<char,int> histogram(string s){
    map<char,int> m;
    for(int i=0;i<s.size();i++){
        m[s[i]]++;
    }
    return m;
}

int main