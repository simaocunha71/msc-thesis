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
	int l=str.length();
	vector<string> prefixVector;
	for(int i=1;i<=l;++i){
		if(is_prefix(str, i)){
			prefixVector.push_back(""+to_string(i));
		}
	}
	return prefixVector;
}