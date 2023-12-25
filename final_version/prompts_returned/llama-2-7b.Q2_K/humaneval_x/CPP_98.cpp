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
	int counter=0,i=0,j=s.length()-1;
	while(i!=-1 && j!=-1)
	{
	    if(s[i] == s[j])
        {
            if((isalpha(s[i])&&isupper(s[i]))){
                counter++;}
        }
		if(!isalpha(s[i])) j--;else j--,i++;}
    return counter+counter%2;
}
int main(){
    string s="abcdefg";
    int i=0;
    for(i=count_upper(s);i!=-1;i++){printf("%d ",i)}return 0;
}