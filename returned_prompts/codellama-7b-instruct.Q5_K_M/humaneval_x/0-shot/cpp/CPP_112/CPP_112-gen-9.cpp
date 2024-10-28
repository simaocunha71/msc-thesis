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

    //Write your code here
    vector<string> v;
    string result;
    bool check;
    for(int i=0;i<s.length();i++){
        if(c.find(s[i])==string::npos){
            result+=s[i];
        }
    }
    check=is_palindrome(result);
    v.push_back(result);
    v.push_back(to_string(check));
    return v;
}
int main(){
    string s,c;
    cin>>s>>c;
    vector<string> result = reverse_delete(s,c);
    cout<<result[0]<<endl;
    cout<<result[1]<<endl;
    return 0;
}
