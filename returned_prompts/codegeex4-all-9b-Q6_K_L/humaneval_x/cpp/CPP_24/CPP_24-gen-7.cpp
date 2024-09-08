/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<iostream>
using namespace std;
int largest_divisor(int n){

B:
/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
using namespace std;
int largest_divisor(int n){

C:
/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<iostream>
using namespace std;
int largest_divisor(int n){

D:
/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<iostream>
using namespace std;
int largest_divisor(int n){
for(int i=n-1;i>0;i--){
	if(n%i==0){
		return i;
	}
}
return -1;
}
int main()
{
	int n;
	cin>>n;
	cout<<largest_divisor(n)<<endl;
	return 0;
}