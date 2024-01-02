/*
Write a function that takes a string and returns true if the string
length is a prime number or false otherwise
Examples
prime_length("Hello") == true
prime_length("abcdcba") == true
prime_length("kittens") == true
prime_length("orange") == false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool prime_length(string str){
	int length=str.size();
	for (int i = 2, j = 0; j < length ; ++i,j++ ){
		if (!isPrime(i)) break;
		else if ((str[j] == i) && isPrime(i)){
			return true;
		}
	}
	return false;
}
int main(){
    string test= "Hello";
    printf("%s\n", test.size());
    bool result = prime_length (test);
    if (result == true)
        printf("prime\n");
    else
        printf("not prime\n");
}