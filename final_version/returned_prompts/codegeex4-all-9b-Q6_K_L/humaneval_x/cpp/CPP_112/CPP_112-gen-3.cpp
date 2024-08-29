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

    vector<string> ans;
    string str="";
    for(int i=0;i<s.length();i++){
        int flag=0;
        for(int j=0;j<c.length();j++){
            if(s[i]==c[j]){
                flag=1;
                break;
            }
        }
        if(flag==0){
            str+=s[i];
        }
    }
    ans.push_back(str);
    ans.push_back("False");
    if(str==string(str.rbegin(),str.rend())){
        ans[1]="True";
    }
    return ans;
}
int main(){
    vector<string> ans=reverse_delete("abcdedcba","ab");
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
    return 0;
}

