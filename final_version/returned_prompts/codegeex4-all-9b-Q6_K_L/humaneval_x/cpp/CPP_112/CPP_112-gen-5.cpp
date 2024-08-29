#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

vector<string> reverse_delete(string s,string c){
    string result;
    for(int i=0;i<s.length();i++){
        if(s[i]!=c[0]&&s[i]!=c[1]){
            result=result+s[i];
        }
    }
    string rev=result;
    reverse(rev.begin(),rev.end());
    if(result==rev){
        return {result,"True"};
    }else{
        return {result,"False"};
    }
}
