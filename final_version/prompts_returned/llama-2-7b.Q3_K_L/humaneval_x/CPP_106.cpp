/*
Implement the function f that takes n as a parameter,
and returns a vector of size n, such that the value of the element at index i is the factorial of i if i is even
or the sum of numbers from 1 to i otherwise.
i starts from 1.
the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
Example:
f(5) == {1, 2, 6, 24, 15}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> f(int n){
	vector<int> a(n);
	for(int i=1;i<n+1;++i)
	{if(i%2==0&&i!=-1)a[i-1]=i*i;else a[i-1]=(i-1)*(i-1);}
	return a;
}