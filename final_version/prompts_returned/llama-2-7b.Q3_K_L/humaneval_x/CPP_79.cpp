/*
You will be given a number in decimal form and your task is to convert it to
binary format. The function should return a string, with each character representing a binary
number. Each character in the string will be '0' or '1'.

There will be an extra couple of characters "db" at the beginning and at the end of the string.
The extra characters are there to help with the format.

Examples:
decimal_to_binary(15)   // returns "db1111db"
decimal_to_binary(32)   // returns "db100000db"
*/
#include<stdio.h>
#include<string>
using namespace std;
string decimal_to_binary(int decimal){
	if (decimal==0) return "0";
    int mask= 1<<(32 - decimal); // mask contains the powers of 2 from last to first
    string res="";
    while((mask>>>0)&1)res+=("1");  
    for(int i=0;i<decimal;++i){
        res+=(char)(((mask>>>0) & 1 ? '1' : '0') ); // mask contains the powers of 2 from last to first
	}
	return "db"+res+"db";
    return "";
}
int main(){
	int a;
	scanf("%d",&a);
	printf(decimal_to_binary(a));
	return 0;
}