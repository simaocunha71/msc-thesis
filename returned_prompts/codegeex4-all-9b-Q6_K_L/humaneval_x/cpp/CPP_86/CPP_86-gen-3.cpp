#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    int i=0,j=0;
    string res="";
    while(i<s.length()){
        string temp="";
        while(i<s.length()&&s[i]!=' '){
            temp+=s[i];
            i++;
        }
        sort(temp.begin(),temp.end());
        res+=temp;
        if(i<s.length()&&s[i]==' ')
            res+=' ';
        i++;
    }
    return res;
}

