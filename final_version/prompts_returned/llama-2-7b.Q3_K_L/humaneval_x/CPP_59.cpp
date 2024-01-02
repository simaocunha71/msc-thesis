/*
Return the largest prime factor of n. Assume n > 1 and is not a prime.
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
*/
#include<stdio.h>
using namespace std;
int largest_prime_factor(int n){
	if(n == 1 || n < 2) return -1;//error check
	int i,count = 0;//i to keep track of the position of the largest prime factor
	int j=2;//j to find if a number is even or odd
	while (n >0){
		if(n%j == 0) {//number is even divide by two and add one
			count++;//if we are dividing by an even number increment our count of factors
			i = i +1; //i to keep track of the position
		}else{//number is odd, check if it's prime
			if(j == 2) return n;//stop when a prime is found
			n = n / j;//if not it's a factor divide by it and add one to the count
			i=0;//reset i so that we can take another look into checking for primeness
		}
	j++; //check again for primeness
	}
	return count ;//return the number of factors in our largest prime factor
}
int main() {
    int n = 13195;
    printf("largest_prime_factor(n):\t%d \n",largest_prime_factor(n));
    return 0;
}
