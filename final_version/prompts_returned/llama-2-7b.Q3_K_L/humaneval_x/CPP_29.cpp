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
	for(int i=0;i<strings.size();++i)
	if(strncmp(strings[i].c_str(),prefix.c_str(),prefix.length()) == 0)
	return true;
	else return false;}
