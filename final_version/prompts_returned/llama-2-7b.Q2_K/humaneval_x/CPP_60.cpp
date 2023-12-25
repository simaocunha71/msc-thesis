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
	int a=1,b=0;
	if (a>=n) return b;
    while (a<=n)
    {
        a++;
        b+=a;
    }
    return b;
}
void main(){
     printf("sum_to_%d() : %d\n",5,sum_to_n(5));
	printf("sum_to_%d() : %d\n",10,sum_to_n(10));
    printf("sum_to_%d() : %d\n",30,sum_to_n(30));
}
