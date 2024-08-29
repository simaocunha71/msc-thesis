#include<stdio.h>
#include<ctype.h>
#include<string>
using namespace std;
string solve(string s){

B:
#include<stdio.h>
#include<ctype.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    for (int i = 0; i < s.length(); i++){
        if (isalpha(s[i])){
            if (islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    if (result.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        string temp = "";
        for (int i = result.length() - 1; i >= 0; i--){
            temp += result[i];
        }
        result = temp;
    }
    return result;

C:
#include<stdio.h>
#include<ctype.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    for (int i = 0; i < s.length(); i++){
        if (isalpha(s[i])){
            if (islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    if (result.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        string temp = "";
        for (int i = result.length() - 1; i >= 0; i--){
            temp += s[i];
        }
        result = temp;
    }
    return result;

D:
#include<stdio.h>
#include<ctype.h>
#include<string>
using namespace std;
string solve(string s){
    string result = "";
    for (int i = 0; i < s.length(); i++){
        if (isalpha(s[i])){
            if (islower(s[i])){
                result += toupper(s[i]);
            }else{
                result += tolower(s[i]);
            }
        }else{
            result += s[i];
        }
    }
    if (result.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        string temp = "";
        for (int i = result.length() - 1; i >= 0; i--){
            temp += result[i];
        }
        result = temp;
    }
    if (result.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == string::npos){
        string temp = "";
        for