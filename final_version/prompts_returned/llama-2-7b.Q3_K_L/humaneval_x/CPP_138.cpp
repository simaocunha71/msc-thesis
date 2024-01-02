/*
Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
Example
is_equal_to_sum_even(4) == false
is_equal_to_sum_even(6) == false
is_equal_to_sum_even(8) == true
*/
#include<stdio.h>
using namespace std;
bool is_equal_to_sum_even(int n){
	if(n==0 || n==1) return 0;

	for(int i=2 ;i<=n/4; i+=2){ // for loop to check if number can be divided by 2 without remainder
		if(n%i==0 && (n!=1 || i!=0)) break;
	}
	return n%i == 0;// returns 0 if it is even, otherwise returns 1

}
int main(){
	printf("%d\n",is_equal_to_sum_even(4));
	return 0;
}