/*
Task
Write a function that takes a string as input and returns the sum of the upper characters only's
ASCII codes.

Examples:
    digitSum("") => 0
    digitSum("abAB") => 131
    digitSum("abcCd") => 67
    digitSum("helloE") => 69
    digitSum("woArBld") => 131
    digitSum("aAaaaXa") => 153
*/
#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){

    int sum=0;
    for(int i=0;i<s.size();i++){
        if(s[i]>='A'&&s[i]<='Z'){
            sum+=s[i];
        }
    }
    return sum;
}

// 2016-11-23 21:37:55

int digitSum(string s){
    int sum = 0;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] >= 'A' && s[i] <= 'Z') {
            sum += s[i];
        }
    }
    return sum;
}

// 2016-11-23 21:42:21

int digitSum(string s){
    int sum = 0;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] >= 'A' && s[i] <= 'Z') {
            sum += s[i];
        }
    }
    return sum;
}

// 2016-11-23 21:43:47

int digitSum(string s){
    int sum = 0;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] >= 'A' && s[i] <= 'Z') {
            sum += s[i];
        }
    }
    return