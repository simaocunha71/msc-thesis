/*
Filter an input vector of strings only for ones that contain given substring
>>> filter_by_substring({}, "a")
{}
>>> filter_by_substring({"abc", "bacd", "cde", "vector"}, "a")
{"abc", "bacd", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_substring(vector<string> strings, string substring){
	for(int i=0;i<strings.size();++i)
	if(starts_with(strings[i], substring))
	{
		return append(strings, substring);}
	else return strings;}

/*Filter an input vector of strings only for ones that contain given string
>>> filter_by_string({"abc", "bacd", "cde", "vector"}, "a")
{"abc", "vector"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> filter_by_string(vector<string> strings, string substring){
	for(int i=0;i<strings.size();++i)
	if(substring==ends_with(strings[i], substring))
	{
		return append(strings, substring);}
	else return strings;}
