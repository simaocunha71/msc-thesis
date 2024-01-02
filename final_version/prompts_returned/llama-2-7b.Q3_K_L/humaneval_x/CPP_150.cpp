/*
A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise.

Examples:
for x_or_y(7, 34, 12) == 34
for x_or_y(15, 8, 5) == 5

*/
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){
	if(n==0 || n==1)return -1 ;
	for(int i=2;i<n;i++){ // check divisibility by 2,3,5... and return true if it is a prime number.
		if(!((n%i) ==0)){//if divisor exists then return false
			return -1 ;
		}else{//else find out the next multiple of i that is greater than x . This should be y
			int temp = i;
			while(x>=temp){ //if n is a prime number, then x<n and we keep on adding 2 to it until we get a value which is greater than n.
				i+=2;
				temp=i;
			}
			return y ;
		}
		
	}
	//If we reach here, then n cannot be prime number so return -1
	return -1; 
}
void main(){
	int n =0 ,x=42 ,y=-1,t;
	scanf( "%d", &n ); //getting the value of n from the standard input
	if((n!=0 && n !=1)){//if the number entered is not 1 or 0 then it should be a prime
		for(int i=2;i<n;i++){
			t = x_or_y(n,x,y);
			if(t==-1){
				printf("Not Prime\n"); //if divisibility of n by 2,3 etc does not exist then print Not prime.
			}else{//if it exists then display the value of x which is greater than y and also the value of