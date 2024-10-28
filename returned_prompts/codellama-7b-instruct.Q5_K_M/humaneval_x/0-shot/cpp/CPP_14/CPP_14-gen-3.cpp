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
    vector<string> result;
    for(int i=0;i<str.size();i++){
        string s;
        for(int j=0;j<=i;j++) s+=str[j];
        result.push_back(s);
    }
    return result;
}
