#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int count_upper(string s){
    int n=s.length();
    int count=0;
    for(int i=0;i<n;i+=2){
        if(s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
            count++;
    }
    return count;
}

