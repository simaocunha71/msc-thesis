/*
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
*/
#include<stdio.h>
using namespace std;
int starts_one_ends(int n){
  int i;
  int count = 0;
  int temp = 1;
  for(i = 0; i < n-2; i++){
    temp *= 9;
  }
  count += temp;
  if(n > 1){
    count += 2;
  }
  return count;
}

int main(){
  int n = 4;
  printf("Count: %d", starts_one_ends(n));
  return 0;
}

B:
/*
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
*/
#include<stdio.h>
using namespace std;
int starts_one_ends(int n){
  int i;
  int count = 0;
  int temp = 1;
  for(i = 0; i < n-2; i++){
    temp *= 9;
  }
  count += temp;
  if(n > 1){
    count += 2;
  }
  return count;
}

int main(){
  int n = 4;
  printf("Count: %d", starts_one_ends(n));
  return 0;
}
