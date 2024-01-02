/*
Given a string representing a space separated lowercase letters, return a map
of the letter with the most repetition and containing the corresponding count.
If several letters have the same occurrence, return all of them.

Example:
histogram("a b c") == {{"a", 1}, {"b", 1}, {"c", 1}}
histogram("a b b a") == {{"a", 2}, {"b", 2}}
histogram("a b c a b") == {{"a", 2}, {"b", 2}}
histogram("b b b b a") == {{"b", 4}}
histogram("") == {}

*/
#include<stdio.h>
#include<string>
#include<map>
using namespace std;
map<char,int> histogram(string test){
	int sum=0;
	for(int i=0;i<strlen(test);i++){
		if(sum==0)
		sum+=test[i];
	}
	return map<char,int>((const char*)test.c_str(),sum);
}
int main(){
	string test="ababab";
	map<char,int> m=histogram(test);
	for(auto it=m.begin();it!=m.end();++it)
	{
		printf("%s : %d\n",it->second.c_str(),it->first);
	}
	return 0;
}
