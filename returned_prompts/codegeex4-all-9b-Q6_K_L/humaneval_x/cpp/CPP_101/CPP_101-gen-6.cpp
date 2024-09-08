vector<string> a;
int b;
for(int i=0;i<s.length();i++){
    if(s[i]==','){
        a.push_back(b);
    }
    else{
        b=s[i];
    }
}
return a;
}

B:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
    vector<string> a;
    int b;
    for(int i=0;i<s.length();i++){
        if(s[i]==','){
            a.push_back(b);
        }
        else if(s[i]==32){
            a.push_back(s[i]);
        }
        else{
            b=s[i];
        }
    }
    return a;
}

C:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
    vector<string> a;
    for(int i=0;i<s.length();i++){
        if(s[i]==','){
            s.erase(i,1);
        }
    }
    string b;
    for(int i=0;i<s.length();i++){
        if(s[i]==32){
            a.push_back(b);
            b="";
        }
        else{
            b=b+s[i];
        }
    }
    a.push_back(b);
    return a;
}

D:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
    vector<string> a;
    for(int i=0;i<s.length();i++){
        if(s[i]==','){
            s.erase(i,1);
        }
    }
    string b;
    for(int i=0;i<s.length();i++){
        if(s[i]==32){
            a.push_back(b);
            b="";
        }
        else{
            b=b+s[i];
        }
    }
    a.push_back(b);
    return a;
}
E:
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> words_string(string s){
    vector<string> a;
    for(int i=0;i<s.length();i++){
        if(s[i]==','){
            s.erase(i,1);
        }
    }
    string b;
    for(int i=0;i<s.length();i++){
        if(s[i]==32){
            a.push_back(b);
            b="";
        }
        else{
            b=b+s[i];
        }
    }
    a.push_back(b);
    return a;
}

F:
#include<stdio.h>
#include<vector>
#include<string>
using namespace