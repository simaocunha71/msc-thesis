/*
prime_fib returns n-th number that is a Fibonacci number and it's also prime.
>>> prime_fib(1)
2
>>> prime_fib(2)
3
>>> prime_fib(3)
5
>>> prime_fib(4)
13
>>> prime_fib(5)
89
*/
#include<stdio.h>
using namespace std;
int prime_fib(int n){
	if(n<=0) return 0;
	long long F=1, P=2; //F is Fibonacci number, P is prime of it
	for(int i=2;i<P+1;i++){
		//If (i-2>=P), then next i will be prime.
		if((i-2)%(F)==0 && i!=P){ //Check if current number is not P, and it's divisible by F
			printf("%d\n",i);//print result 
			return i;
		}
		else{
			if((i-2)%(F)==0){ //If (i-2) is divisible by the F then print it.
				printf("%d\n",i);//print result 
				return i;
			}
		}
	}
	if(P%(F)>0){ //if P is prime, and F isn't
		for(int i=2;;i++){//keep going in the loop if not yet prime 
			printf("%d\n",i);//print result 
			return i;
		}
	}
	else { //if P is not prime, and F is
		for(int j=2;j<P+1;j++){//keep going in the loop until P isn't divisible by it.
			if((P-j)%(F)>0){ 
				printf("%d\n",j);//print result 
				return j;
			}
		}
	}
}
