/*
Given a positive integer n, return the product of the odd digits.
Return 0 if all digits are even.
For example:
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
*/
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
	if(n==0||n==1||n==-1 )return 0;
	int ret=0,i,j,c=0,p=0;
	for (i = 1; i <= n; i++) {
		c += String::toInt(char(i));
	}
	if(c==0){
	return 0;}else{
	int oddC=String::toInt(char(n%2))-1;
	for (j = oddC ; j > -1 && j < i ; j--) {
		p += String::toInt(char(j));
	}
	ret+=p*i;} 
}
int main(){
    int n,res=0;
    cout<<"n="<<endl;
    cin>>n;
    cout<<digits(n)<<endl;
return 0;
	}
	// #include<iostream>
/*	using namespace std;*/