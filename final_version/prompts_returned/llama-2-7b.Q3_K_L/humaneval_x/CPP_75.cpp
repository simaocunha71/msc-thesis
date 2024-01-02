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
	if(a==1 || a==2|| a==5) {return false;}
	else{
    int i,j;
    
    for(i=3;i<=sqrt(a);i++){
        if((a%i)==0) {
            printf("%d ",i);
             if(is_multiply_prime(i)) return true;
        }
         else {
             	return false;
        }
    }
}  
	return false;
}
int main(){
    int a,i=3;
	printf("Enter number: ");
	scanf("%d",&a);
    if(is_multiply_prime(a)) printf("true");
	else printf("false");
	return 0;
}