#include<stdio.h>
#include<math.h>
#include<string.h>
#include<string>
#include<stdlib.h>
using namespace std;
int fruit_distribution(string s,int n){
    int a=0,b=0;
    for(int i=0;i<s.length();i++){
        if(s[i]>='0'&&s[i]<='9'){
            if(s[i+1]>='0'&&s[i+1]<='9'){
                if(a==0)
                    a=(s[i]-'0')*10+(s[i+1]-'0');
                else
                    b=(s[i]-'0')*10+(s[i+1]-'0');
            }
            else if(a==0)
                a=s[i]-'0';
            else
                b=s[i]-'0';
        }
    }
    return n-a-b;
}