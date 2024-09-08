#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string solve(string s){
    int len = s.length();
    for(int i=0; i<len; i++){
        if(s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z'){
            if(s[i] >= 'a' && s[i] <= 'z'){
                s[i] = s[i] - 32;
            }
            else{
                s[i] = s[i] + 32;
            }
        }
    }
    if(len == 0){
        reverse(s.begin(), s.end());
    }
    return s;
}

B:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string solve(string s){
    int len = s.length();
    for(int i=0; i<len; i++){
        if(s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z'){
            if(s[i] >= 'a' && s[i] <= 'z'){
                s[i] = s[i] - 32;
            }
            else{
                s[i] = s[i] + 32;
            }
        }
    }
    if(len != 0){
        reverse(s.begin(), s.end());
    }
    return s;
}

C:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string solve(string s){
    int len = s.length();
    for(int i=0; i<len; i++){
        if(s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z'){
            if(s[i] >= 'a' && s[i] <= 'z'){
                s[i] = s[i] - 32;
            }
            else{
                s[i] = s[i] + 32;
            }
        }
    }
    if(len == 0){
        reverse(s.begin(), s.end());
    }
    return s;
}

D:
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string solve(string s){
    int len = s.length();
    for(int i=0; i<len; i++){
        if(s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z'){
