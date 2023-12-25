/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
using namespace std;
int largest_divisor(int n){
	if(n==0||n==1)return 0;
        int a=2,b=a+1;
                while((a%b)=0&&b<=n){
                    b+=a;
                }
                 if(a!=b-1||(b>n/2)) return b;
                else return largest_divisor(b); 
}
int main(){
	int n,l=0,b=largest_divisor(15),i;
        printf("Enter the number: \n");scanf("%d",&n);
                 if(n!=0&&n==1)return 0;
                for(i=2;i<=b-1;i++)if((b%i)==0)l+=i;
                if(l>b) b=largest_divisor(l);
	printf("The largest number that divides the given number is: %d\n",b);
        getchar();getch();
	return 0;
}