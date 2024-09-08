#include<stdio.h>
#include<ctype.h>
using namespace std;
int digitSum(string s){
    int sum=0;
    for(int i=0;i<s.size();i++)
    {
        if(isupper(s[i]))
        {
            sum+=s[i];
        }
    }
    return sum;
}