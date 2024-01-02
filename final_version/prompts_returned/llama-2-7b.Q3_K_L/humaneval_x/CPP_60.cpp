/*
sum_to_n is a function that sums numbers from 1 to n.
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
*/
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
	int a = 0, b = 1;
	for(int i=1;i<=n;b++,a+=b,i++)
	{
		if(a%2 == 0) printf("%d ",a);
	}
}
int main(){
	printf("\nsum_to_n(%d)\n",sum_to_n(5));
	return 0;
}
