/*
Circular shift the digits of the integer x, shift the digits right by shift
and return the result as a string.
If shift > number of digits, return digits reversed.
>>> circular_shift(12, 1)
"21"
>>> circular_shift(12, 2)
"12"
*/
#include<stdio.h>
#include<string>
using namespace std;
string circular_shift(int x,int shift){
	if(x==0) return "0";
	int reminder=((x%10)+shift)%10+1;
	while(reminder>=10)reminder-=10;
	char temp[3];
	int i=0,j=0,k=0;
	if(shift==0){
		temp[i]=x%10+'0';
		circular_shift(x/10,shift);
	}else{
		for(;x>=10;x-=10)
		{
			if((x%10)+shift<=10){
				temp[i]+=(x%10+'0');
				circular_shift(x/10,shift);
			}else{
				temp[j]='0';
				for(k=2;((x%10)+shift)>10;k++)
				{
					if(x<=9)circular_shift(x+k,shift);
				}
				temp[j]=(x%10+'0');
				circular_shift(x/10,shift+1);//If shift==0 then 2*shift.
				for(;k>4;k--)
				{
				if((x%10)+shift>=10){
					temp[j]=(x%10+'0');
				}else break;
				circular_shift(x/10,shift);//If shift==1 then (2*shift)+