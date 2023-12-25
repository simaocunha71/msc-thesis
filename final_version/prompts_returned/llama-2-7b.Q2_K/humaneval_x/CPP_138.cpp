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
	if(n%2==0 && n!=0) {
   int a[4]={1, 2, 3 ,4};
   for (int i=0;i<4;++i) {
      if (a[i]*2>=n && a[i]!=0 ) {
        // printf("sum of %d and %d is %d\n", a[i-1], a[i-1]+a[i], n);
        return true;  
     }
    else if (a[3]*2>=n && a[3]!=0) {
      printf("sum of %d and %d is %d\n", a[3-1], a[3-1]+a[3], n);
     return true;  
    }
  }
  else if (n==0) {
   //printf("\nno even numbers can sum to 0\n");
   return false;  
  } 
  else {
    printf("sum of %d and %d is not an even number.\n", a[3-1], a[3-1]+a[3]);    //n+4, n,2n are the values
     return false;    
  }
}	  
int main(){
    int i=0;
    int n;
    printf("enter the number: ");
     scanf("%d", &n);
  while(i < 4) {
      if (a[i]!=0 && a[i]==n-a[i+1]) {
        //printf("Sum of %d and %d is %d\n",a[i], n-a[i], sum);  
      }else{
         printf("%s not an even number.\n",  a[i]);
     }