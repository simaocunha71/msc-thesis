/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})

>>> longest({"a", "b", "c"})
"a"
>>> longest({"a", "bb", "ccc"})
"ccc"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string longest(vector<string> strings){
	if(strings.size()==0) return "";
	int maxLength=INT_MIN;
	for(auto iter:strings){
		int len = strlen(iter.c_str());
		if(maxLength < len){
			maxLength = len;
		}
	}
	return strings[0];
}
