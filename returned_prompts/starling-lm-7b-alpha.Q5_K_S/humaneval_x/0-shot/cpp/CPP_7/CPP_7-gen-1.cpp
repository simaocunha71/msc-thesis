	vector<string> res;
	for(int i = 0; i < strings.size(); i++){
		if(strings[i].find(substring) != std::string::npos)
			res.push_back(strings[i]);
	}
	return res;
}




/*
Given a string, generate all its permutations
>>> gen_permutations("abc")
["abc", "bac", "bca", "acb", "cab", "cba"]
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> gen_permutations(string s){
	if(s.size() == 0)
		return vector<string>();
	if(s.size() == 1)
		return vector<string>(1, s);
	vector<string> res;
	for(int i = 0; i < s.size(); i++){
		string tmp = s;
		tmp.erase(i, 1);
		for(string x : gen_permutations(tmp))
			res.push_back(s[i] + x);
	}
	return res;
}




/*
Given a string, count how many times a substring appears in it
>>> count_substring({"abc", "bacd", "cde", "vector"}, "a")
3

>>> count_substring({"abc", "bacd", "cde", "vector"}, "z")
0

>>> count_substring({"abc", "bacd", "cde", "vector"}, "")
4

>>> count_substring({"abc", "bacd", "cde", "vector"}, "abc")
1

>>> count_substring({"abc", "bacd", "cde", "vector"}, "ab")
2
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int count_substring(vector<string> strings, string substring){
	int res = 0;
	for