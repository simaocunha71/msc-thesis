/*
Return vector of all prefixes from shortest to longest of the input string
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> all_prefixes(string str){
    vector<string> result;
    for (int i = 0; i < str.size(); ++i) {
        string prefix = str.substr(0, i + 1);
        result.push_back(prefix);
    }
    return result;
}
