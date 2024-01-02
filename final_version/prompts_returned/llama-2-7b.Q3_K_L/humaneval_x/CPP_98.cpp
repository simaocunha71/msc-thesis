/*
Given a string s, count the number of uppercase vowels in even indices.

For example:
count_upper("aBCdEf") returns 1
count_upper("abcdefg") returns 0
count_upper("dBBE") returns 0
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int count_upper(string s){
	int res = 0;
	for (size_t i = 1 ; i < s.length() ; i += 2) { // Even Indices
		if ((s[i] >= 'A' && s[i] <= 'Z') || (s[i+1] >= 'A' && s[i+1] <= 'Z')){
			res++;
		}
	}
	return res;
}
int main(){
	printf("%d\n",count_upper("aBCdEf"));
	return 0;
}