#include<stdio.h>
#include<string>
using namespace std;
string encrypt(string s){

    int l = s.length();
    string t = "";
    for(int i = 0; i < l; i++) {
        if(s[i] >= 'a' && s[i] <= 'z') {
            t += (char)(((s[i] - '