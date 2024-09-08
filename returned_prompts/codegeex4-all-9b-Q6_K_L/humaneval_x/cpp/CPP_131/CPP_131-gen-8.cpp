#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
    int ans=1;
    string s=to_string(n);
    for(int i=0;i<s.size();i++){
        if(s[i]%2!=0) ans*=s[i];
    }
    if(ans==0) return 0;
    else return ans;
}