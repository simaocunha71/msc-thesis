/*
Filter an input vector of strings only for ones that start with a given prefix.
>>> filter_by_prefix({}, "a")
{}
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i = 0; i < strings.size(); i++){
        if (strings[i].find(prefix) == 0){
            result.push_back(strings[i]);
        }
    }
    return result;
}

B:
/*
Filter an input vector of strings only for ones that start with a given prefix.
>>> filter_by_prefix({}, "a")
{}
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i = 0; i < strings.size(); i++){
        if (strings[i].substr(0, prefix.length()) == prefix){
            result.push_back(strings[i]);
        }
    }
    return result;
}

C:
/*
Filter an input vector of strings only for ones that start with a given prefix.
>>> filter_by_prefix({}, "a")
{}
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i = 0; i < strings.size(); i++){
        if (strings[i].compare(0, prefix.length(), prefix) == 0){
            result.push_back(strings[i]);
        }
    }
    return result;
}

D:
/*
Filter an input vector of strings only for ones that start with a given prefix.
>>> filter_by_prefix({}, "a")
{}
>>> filter_by_prefix({"abc", "bcd", "cde", "vector"}, "a")
{"abc", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (int i = 0; i < strings.size();