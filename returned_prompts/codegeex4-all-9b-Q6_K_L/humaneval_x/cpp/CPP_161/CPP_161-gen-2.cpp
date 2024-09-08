#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    int len = s.length();
    for(int i = 0; i < len; i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    if(result.find_first_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        for(int i = len - 1; i >= 0; i--){
            result += s[i];
        }
    }
    return result;
}
C:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    int len = s.length();
    for(int i = 0; i < len; i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    if(result.find_first_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        for(int i = len - 1; i >= 0; i--){
            result += s[i];
        }
    }
    return result;
}
D:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    int len = s.length();
    for(int i = 0; i < len; i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    if(result.find_first_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        for(int i = len - 1; i >= 0; i--){
            result += s[i];
        }
    }
    return result;
}
E:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    int len = s.length();
    for(int i = 0; i < len; i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
       