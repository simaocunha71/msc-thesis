/*
Given a string s, count the number of uppercase vowels in even indices.

For example:
count_upper("aBCdEf") returns 1
count_upper("abcdefg") returns 0
count_upper("dBBE") returns 0
*/
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int count_upper(string s){
    int count=0;
    for(int i=0;i<s.length();i++){
        if(i%2==0){
            if(s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
            count++;
        }
    }
    return count;
}
int main(){
    string s;
    cin>>s;
    cout<<count_upper(s)<<endl;
    return 0;
}