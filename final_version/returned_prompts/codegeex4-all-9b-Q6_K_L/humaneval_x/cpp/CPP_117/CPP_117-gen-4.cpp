#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> v;
    string consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    string word;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            if(count(word.begin(),word.end(),consonant) == n){
                v.push_back(word);
            }
            word = "";
        }
        else{
            word+=s[i];
        }
    }
    return v;
}

B:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> v;
    string consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    string word;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            if(count(word.begin(),word.end(),consonant) == n){
                v.push_back(word);
            }
            word = "";
        }
        else{
            word+=s[i];
        }
    }
    return v;
}

C:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> v;
    string consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    string word;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            if(count(word.begin(),word.end(),consonant) == n){
                v.push_back(word);
            }
            word = "";
        }
        else{
            word+=s[i];
        }
    }
    return v;
}

D:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> v;
    string consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
    string word;
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            if(count(word.begin(),word.end(),consonant) == n){
                v.push_back(word);
            }
            word = "";
        }
        else{
            word+=s[i