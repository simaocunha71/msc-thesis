/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
*/
#include<stdio.h>
#include<string>
using namespace std;
int how_many_times(string str,string substring){
	int sub=0;
	for(int i = 1;i<=str.length();++i)
	{sub+=sub&1? (str[i-1]==substring[0]) : 0;}
	if(sub%2==1)
    printf("%d\n", (sub+1)/2);
	return sub;
}
main(){how_many_times("aaaa","aa");}