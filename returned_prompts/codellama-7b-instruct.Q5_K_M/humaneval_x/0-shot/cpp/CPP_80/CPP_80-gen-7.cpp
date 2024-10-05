/*
You are given a string s.
Your task is to check if the string is happy or not.
A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
For example:
is_happy("a") => false
is_happy("aa") => false
is_happy("abcd") => true
is_happy("aabb") => false
is_happy("adb") => true
is_happy("xyy") => false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool is_happy(string s){
    int n=s.length();
    if(n<3) return false;
    int j=0;
    for(int i=0;i<n-3;i++){
        if(s[i]==s[i+1] && s[i+1]==s[i+2]){
            j=1;
            break;
        }
    }
    return !j;
}
