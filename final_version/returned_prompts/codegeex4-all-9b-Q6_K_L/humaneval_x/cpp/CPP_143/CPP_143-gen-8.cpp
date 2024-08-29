#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string s;
    string result;
    int i=0;
    int len = sentence.length();
    while(i<len){
        if(sentence[i]==' '){
            if(prime(s.length())){
                result += s;
            }
            s="";
            i++;
            continue;
        }
        s += sentence[i];
        i++;
    }
    if(s.length()!=0){
        if(prime(s.length())){
            result += s;
        }
    }
    return result;
}
bool prime(int n){
    if(n==1||n==0){
        return false;
    }
    for(int i=2;i<n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

B:
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string s;
    string result;
    int i=0;
    int len = sentence.length();
    while(i<len){
        if(sentence[i]==' '){
            if(prime(s.length())){
                result += s;
            }
            s="";
            i++;
            continue;
        }
        s += sentence[i];
        i++;
    }
    if(s.length()!=0){
        if(prime(s.length())){
            result += s;
        }
    }
    return result;
}
bool prime(int n){
    if(n==1||n==0){
        return false;
    }
    for(int i=2;i<n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

C:
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string s;
    string result;
    int i=0;
    int len = sentence.length();
    while(i<len){
        if(sentence[i]==' '){
            if(prime(s.length())){
                result += s;
            }
            s="";
            i++;
            continue;
        }
        s += sentence[i];
        i++;
    }
    if(s.length()!=0){
        if(prime(s.length())){
            result += s;
        }
    }
    return result;
}
bool prime(int n){
    if(n==1||n==0){
        return false;
    }
    for(int i=2;i<n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

D:
#include<stdio.h>
#include<string>
using