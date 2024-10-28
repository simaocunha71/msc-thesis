  if(a==round(a) && b==round(b) && c==round(c)){
    if(a==b+c || b==a+c || c==a+b)
      return true;
  }
  return false;
}

int main() {
  printf("%d", any_int(5, 2, 7));
  printf("%d", any_int(3, 2, 2));
  printf("%d", any_int(3, -2, 1));
  printf("%d", any_int(3.6, -2.2, 2));
  return 0;
}

// QUESTION :
/*
Create a function that takes two arrays of positive numbers and returns the average of the sum of the two arrays.

Examples
average_sum([1, 2, 3, 4], [5, 6, 7, 8]) ➞ 11.5
average_sum([15, 9, 6], [6, 14, 15]) ➞ 13.5
average_sum([2, 4, 6, 8], [10, 12, 14, 16]) ➞ 12.5

Notes
Arrays will have at least one element.

*/

#include<stdio.h>
using namespace std;
float average_sum(int a[],int b[],int size_a,int size_b){
  int sum_a=0,sum_b=0;
  for(int i=0;i<size_a;i++)
    sum_a+=a[i];
  for(int i=0;i<size_b;i++)
    sum_b+=b[i];
  return (sum_a+sum_b)/2.0;
}

int main() {
  int a[] = {1, 2, 3, 4};
  int b[] = {5, 6, 7, 8};
  printf("%f", average_sum(a, b, 4, 4));
 