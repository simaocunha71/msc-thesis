/*
Given a string of words, return a vector of words split on whitespace, if no whitespaces exists in the text you
should split on commas ',' if no commas exists you should return a vector with one element, the number of lower-case letters with odd order in the
alphabet, ord("a") = 0, ord("b") = 1, ... ord("z") = 25
Examples
split_words("Hello world!") ➞ {"Hello", "world!"}
split_words("Hello,world!") ➞ {"Hello", "world!"}
split_words("abcdef") == {"3"} 
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
vector<string> split_words(string txt){
	int size = (int)txt.size();
	vector<string> svec;
	for(int i = 0;i < size -1;++i){
		if(txt[i] == ' ') break;
	}
	svec.push_back(txt.substr(0,i));
	return svec;
};
int main(){
	string str = "Hello world!";
	vector<string> wvctr = split_words(str);
	for(auto i :wvctr) cout<<i<<" ";
}