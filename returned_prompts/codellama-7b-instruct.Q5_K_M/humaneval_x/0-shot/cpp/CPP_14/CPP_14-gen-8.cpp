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
    result.push_back("");
    for(int i=0;i<str.size();i++)
        for(int j=0;j<result.size();j++)
            result.push_back(result[j]+str[i]);
    return result;
}

