#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
string result = "";
for(int i = 0; i < s.length(); i++){
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
if(!isalpha(s[0])){
    reverse(result.begin(), result.end());
}
return result;

B:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
string result = "";
for(int i = 0; i < s.length(); i++){
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
if(isalpha(s[0])){
    reverse(result.begin(), result.end());
}
return result;

C:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
string result = "";
for(int i = 0; i < s.length(); i++){
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
if(isdigit(s[0])){
    reverse(result.begin(), result.end());
}
return result;

D:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
string result = "";
for(int i = 0; i < s.length(); i++){
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
if(!isalpha(s[0]) && !isdigit(s[0])){
    reverse(result.begin(), result.end());
}
return result;

E:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
string result = "";
for(int i = 0; i < s.length(); i++){
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
if(isalpha(s