  if(n==1) return 1;
  if(n==2) return 2;
  if(n%2==0) return 2*(n/2)*(n/2);
  if(n%2==1) return 2*(n/2)*(n/2+1);
}
int main(){
  int n;
  scanf("%d",&n);
  printf("%d",starts_one_ends(n));
}

Ans:
/*
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
*/
#include<stdio.h>
using namespace std;
int starts_one_ends(int n){
  int count=0;
  for(int i=1;i<=n;i++)
  {
    for(int j=1;j<=n;j++)
    {
      if(i==1||i==n) count++;
      if(j==1||j==n) count++;
    }
  }
  return count;
}
int main(){
  int n;
  scanf("%d",&n);
  printf("%d",starts_one_ends(n));
}
