/*
Return a string containing space-delimited numbers starting from 0 upto n inclusive.
>>> string_sequence(0)
"0"
>>> string_sequence(5)
"0 1 2 3 4 5"
*/
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
	if(n == 0) return "0";
	if(n%2==0) return string_sequence(n/2)+"-"+string_sequence((n-1)/2);
	return string_sequence(n/2)+" "+string_sequence((n-1)/2);
}
int main(){
	printf("The sequence of numbers: \n");
	printf("%s\n",string_sequence(5));
	return 0;
}