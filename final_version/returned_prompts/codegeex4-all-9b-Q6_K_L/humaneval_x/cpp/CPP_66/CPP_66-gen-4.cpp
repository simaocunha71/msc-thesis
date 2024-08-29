#include<stdio.h>
#include<string>
using namespace std;
int digitSum(string s){
    int sum=0;
    for(int i=0;i<s.length();i++){
        if(s[i]>=65 && s[i]<=90){
            sum+=s[i];
        }
    }
    return sum;
}