#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result;
    bool hasLetter = false;
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            hasLetter = true;
            if(islower(s[i])){
                result += toupper(s[i]);
            }
            else{
                result += tolower(s[i]);
            }
        }
        else{
            result += s[i];
        }
    }
    if(!hasLetter){
        reverse(result.begin(), result.end());
    }
    return result;
}

B:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result;
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }
            else{
                result += tolower(s[i]);
            }
        }
        else{
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
    string result;
    bool hasLetter = false;
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            hasLetter = true;
            if(islower(s[i])){
                result += toupper(s[i]);
            }
            else{
                result += tolower(s[i]);
            }
        }
        else{
            result += s[i];
        }
    }
    if(!hasLetter){
        string temp;
        for(int i=s.length()-1; i>=0; i--){
            temp += s[i];
        }
        return temp;
    }
    return result;
}

D:
#include<stdio.h>
#include<string>
using namespace std;
string solve(string s){
    string result;
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                result += toupper(s[i]);
            }
            else{
                result += tolower(s[i]);
            }
        }
        else{
            result += s[i];
        }
    }
    string temp;
    for(int i=s.length()-1; i>=0; i--){
        temp += s[i];
    }
    return temp;
}

The correct answer is C.

The function should return the string with reversed case for each letter, and if no letters are found, the string should be reversed. 

Option A is