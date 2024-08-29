#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string temp = "";
    string res = "";
    for(int i=0;i<s.length();i++){
        if(s[i] == ' '){
            temp = temp + s[i];
            res = res + temp;
            temp = "";
        }
        else{
            temp = temp + s[i];
        }
    }
    if(temp != "")
        res = res + temp;
    for(int i=0;i<res.length();i++){
        if(res[i] == ' '){
            sort(res.begin()+i+1,res.end());
        }
    }
    return res;
}

B:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string temp = "";
    string res = "";
    for(int i=0;i<s.length();i++){
        if(s[i] == ' '){
            temp = temp + s[i];
            res = res + temp;
            temp = "";
        }
        else{
            temp = temp + s[i];
        }
    }
    if(temp != "")
        res = res + temp;
    for(int i=0;i<res.length();i++){
        if(res[i] == ' '){
            sort(res.begin()+i+1,res.end());
        }
    }
    return res;
}

C:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string temp = "";
    string res = "";
    for(int i=0;i<s.length();i++){
        if(s[i] == ' '){
            temp = temp + s[i];
            res = res + temp;
            temp = "";
        }
        else{
            temp = temp + s[i];
        }
    }
    if(temp != "")
        res = res + temp;
    for(int i=0;i<res.length();i++){
        if(res[i] == ' '){
            sort(res.begin()+i+1,res.end());
        }
    }
    return res;
}

D:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    string temp = "";
    string res = "";
    for(int i=0;i<s.length();i++){
        if(s[i] == ' '){
            temp = temp + s[i];
            res = res + temp;
            temp = "";
        }
        else{
            temp = temp + s[i];
