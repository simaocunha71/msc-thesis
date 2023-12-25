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
	int cnt=0;
	for (int i=0 ;i<test.length();i++){
		if(i==1 || i==4) continue;
		cnt++;
	}
	return map<char,int>(make_pair('a',cn));
}
// 1. 2. 3. 4. 5.  6.  7.  8.  9.  10.  11.  12.  13.  14. 	15.  16. 	17.
int main(void) {

	return histogram("a b c");
}