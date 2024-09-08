#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    int cnt=0;
    vector<string> res;
    string temp="";
    for(int i=0;i<s.size();i++){
        if(isalpha(s[i])){
            if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') continue;
            temp+=s[i];
            cnt++;
            if(cnt==n){
                res.push_back(temp);
                cnt=0;
                temp="";
            }
        }
    }
    return res;
}
