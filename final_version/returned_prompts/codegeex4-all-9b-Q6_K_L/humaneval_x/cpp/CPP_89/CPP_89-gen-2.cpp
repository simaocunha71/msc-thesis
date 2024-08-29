/*
Create a function encrypt that takes a string as an argument and
returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters 
shift down by two multiplied to two places.
For example:
encrypt("hi") returns "lm"
encrypt("asdfghjkl") returns "ewhjklnop"
encrypt("gf") returns "kj"
encrypt("et") returns "ix"
*/
#include<stdio.h>
#include<string>
using namespace std;
string encrypt(string s){
    string result="";
    for(int i=0;i<s.length();i++){
        if(s[i]>=97 && s[i]<=122){
            result+=((s[i]-97+2*2)%26)+97;
        }
        else if(s[i]>=65 && s[i]<=90){
            result+=((s[i]-65+2*2)%26)+65;
        }
    }
    return result;
}
int main(){
    string s="hi";
    printf("%s\n",encrypt(s).c_str());
    return 0;
}