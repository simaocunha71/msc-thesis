/*
Return vector of all prefixes from shortest to longest of the input string
>>> all_prefixes("abc")
{"a", "ab", "abc"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> ans;
    for(int i=0;i<str.length();i++){
        string temp;
        for(int j=0;j<=i;j++){
            temp+=str[j];
            ans.push_back(temp);
        }
    }
    return ans;
}

