/*
Write a function that returns true if the given number is the multiplication of 3 prime numbers
and false otherwise.
Knowing that (a) is less then 100. 
Example:
is_multiply_prime(30) == true
30 = 2 * 3 * 5
*/
#include<stdio.h>
using namespace std;
bool is_multiply_prime(int a){
	if(a <= 100 && (a % 2 ) != 0 ){
		return (a == 3);
	}else{
		return false;
	}
}
