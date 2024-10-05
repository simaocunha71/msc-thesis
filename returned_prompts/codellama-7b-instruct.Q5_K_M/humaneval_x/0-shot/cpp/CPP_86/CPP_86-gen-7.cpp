/*
Write a function that takes a string and returns an ordered version of it.
Ordered version of string, is a string where all words (separated by space)
are replaced by a new word where all the characters arranged in
ascending order based on ascii value.
Note: You should keep the order of words and blank spaces in the sentence.

For example:
anti_shuffle("Hi") returns "Hi"
anti_shuffle("hello") returns "ehllo"
anti_shuffle("Hello World!!!") returns "Hello !!!Wdlor"
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
string anti_shuffle(string s){
    int n=s.size();
    int i;
    for(i=0;i<n;i++){
        if(s[i]==' ')
            break;
    }
    string a=s.substr(0,i);
    string b=s.substr(i+1,n);
    string c=b;
    int k=0;
    for(int j=0;j<c.size();j++){
        if(c[j]==' '){
            k=j;
            break;
        }
    }
    string d=c.substr(k+1,n);
    string e=c.substr(0,k);
    sort(a.begin(),a.end());
    sort(d.begin(),d.end());
    sort(e.begin(),e.end());
    string res=a+d+e;
    return res;
}
int main(){
    string s="Hello World!!!";
    string r=anti_shuffle(s);
    printf("%s",r.c_str());
}
