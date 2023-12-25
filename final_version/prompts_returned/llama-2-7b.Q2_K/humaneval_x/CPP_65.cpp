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
	if(x==0) return "";
	if(!x/pow(10,shift)) return "0";
	string res = to_string((long long int)x);
	for (int i=res.length()-1;i>=0;--i) 
	{
        res[i]=(res[i+1])>>(8-i);//shifts digits to right by shift
    }
	return res; //convert the string back to integer and return it.
}
int main(){
	int a = 4321,b=900;
	printf("%d\n",circular_shift(a,b));
	return 0;
}