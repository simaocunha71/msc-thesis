/*
Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
the last couple centuries. However, what people don't know is Tribonacci sequence.
Tribonacci sequence is defined by the recurrence:
tri(1) = 3
tri(n) = 1 + n / 2, if n is even.
tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
For example:
tri(2) = 1 + (2 / 2) = 2
tri(4) = 3
tri(3) = tri(2) + tri(1) + tri(4)
       = 2 + 3 + 3 = 8 
You are given a non-negative integer number n, you have to a return a vector of the 
first n + 1 numbers of the Tribonacci sequence.
Examples:
tri(3) = {1, 3, 2, 8}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
	if(n == 0 || n == 1)
		return vec{};
	else if(n < 2)
		return {1,3,-1};
	else
		return tri(n-1)+tri(n-2)+tri(n+1);
}
int main(){
    int n;
	scanf("%d",&n);
	if(n == 0 || n == 1)
		printf("Returning the vector {}\n");
	else if(n < 2)
        printf("Returning the vector {1,3,-1}\n");
	else{
        printf("%d\t",tri(n-1));
        for(int i = n;i>0;i--){
            printf("%d ",tri(i));
        }
    }
}