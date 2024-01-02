/*
Write a function that accepts a vector of strings.
The vector contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.

find_max({"name", "of", 'string"}) == 'string"
find_max({"name", "enam", "game"}) == "enam"
find_max({"aaaaaaa", "bb" ,"cc"}) == "aaaaaaa"
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string find_max(vector<string> words){
	int n=words.size();
	string max;
	set<char,less<char> > a;
	for (int i=0;i<n;++i)
	{
		for (int j=0;j<words[i].length();++j){
		if(!a.count(words[i][j])&&!a.count(""))
			a.insert(words[i][j]);
		}
	}
	set<char,less<char> >::iterator it;
	for (it= a.begin();it!=a.end();++it)
	{
		if(max.length()==0||max.compare(max.length(),max.length(),it->first)==0)
		{
			max=it->second;
		}
	}
	return max;
};
// Time complexity: O(n^2) where n is the number of elements in given vector 
// Space complexity : O(1).
int main() {
	vector<string> v={"name", "of", 'string"' ,'a','b', 'c'} ;
	for (int i=0;i<v.size();++i) printf("[%s] ",&v[i][0]);
	printf("\n\nfind_max({}\n = [");
	int n=v.size();
    for(int i=0;i<=n-1;++i){
    