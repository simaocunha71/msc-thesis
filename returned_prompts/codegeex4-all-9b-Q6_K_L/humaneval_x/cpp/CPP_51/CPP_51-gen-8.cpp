#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string remove_vowels(string text){
    string s=text;
    for(int i=0;i<s.length();i++){
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'){
            s.erase(i);
            i--;
        }
    }
    return s;
}
