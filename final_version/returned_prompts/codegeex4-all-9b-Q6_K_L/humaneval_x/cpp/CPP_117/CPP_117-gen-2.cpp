/*
Given a string s and a natural number n, you have been tasked to implement 
a function that returns a vector of all words from string s that contain exactly 
n consonants, in order these words appear in the string s.
If the string s is empty then the function should return an empty vector.
Note: you may assume the input string contains only letters and spaces.
Examples:
select_words("Mary had a little lamb", 4) ==> {"little"}
select_words("Mary had a little lamb", 3) ==> {"Mary", "lamb"}
select_words('simple white space", 2) ==> {}
select_words("Hello world", 4) ==> {"world"}
select_words("Uncle sam", 3) ==> {"Uncle"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){

    vector<string> vs;
    string str;
    int cnt=0;
    int len=s.length();
    for(int i=0;i<len;i++){
        if(s[i]==' '){
            vs.push_back(str);
            str="";
        }
        else{
            str=str+s[i];
            if(s[i]<'a' || (s[i]>'z' && s[i]<'A') || s[i]>'Z'){
                cnt++;
            }
        }
    }
    if(cnt==n){
        vs.push_back(str);
    }
    return vs;
}

B:
/*
Given a string s and a natural number n, you have been tasked to implement 
a function that returns a vector of all words from string s that contain exactly 
n consonants, in order these words appear in the string s.
If the string s is empty then the function should return an empty vector.
Note: you may assume the input string contains only letters and spaces.
Examples:
select_words("Mary had a little lamb", 4) ==> {"little"}
select_words("Mary had a little lamb", 3) ==> {"Mary", "lamb"}
select_words('simple white space", 2) ==> {}
select_words("Hello world", 4) ==> {"world"}
select_words("Uncle sam", 3) ==> {"Uncle"}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> select_words(string s,int n){
    vector<string> vs;
    string str;
    int cnt=0;
    int len=s.length();
    for(int i=