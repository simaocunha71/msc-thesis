/*
Task
We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
then check if the result string is palindrome.
A string is called palindrome if it reads the same backward as forward.
You should return a vector containing the result string and "True"/"False" for the check.
Example
For s = "abcde", c = "ae", the result should be ("bcd","False")
For s = "abcdef", c = "b"  the result should be ("acdef","False")
For s = "abcdedcba", c = "ab", the result should be ("cdedc","True")
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> reverse_delete(string s,string c){
    int n = s.length();
    int m = c.length();
    vector<string> v;
    string res = "";
    for(int i=0;i<n;i++){
        if(find(c.begin(),c.end(),s[i])==c.end()){
            res += s[i];
        }
    }
    if(res.length()>0){
        reverse(res.begin(),res.end());
    }
    v.push_back(res);
    v.push_back(is_palindrome(res)?"True":"False");
    return v;
}
bool is_palindrome(string s){
    int n = s.length();
    for(int i=0;i<n;i++){
        if(s[i]!=s[n-i-1]){
            return false;
        }
    }
    return true;
}
int main(){
    string s;
    string c;
    cin>>s>>c;
    vector<string> v = reverse_delete(s,c);
    cout<<v[0]<<endl;
    cout<<v[1]<<endl;
    return 0;
}
