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
    if(s.length()<3)
        return false;
    int i=0;
    while(i<s.length()-2){
        string a=s.substr(i,3);
        if(a.length()==3)
            if(a.compare(s.substr(i+1,3))==0)
                return false;
        i++;
    }
    return true;
}


