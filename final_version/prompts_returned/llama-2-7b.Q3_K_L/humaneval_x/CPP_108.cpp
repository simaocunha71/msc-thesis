/*
Write a function count_nums which takes a vector of integers and returns
the number of elements which has a sum of digits > 0.
If a number is negative, then its first signed digit will be negative:
e.g. -123 has signed digits -1, 2, and 3.
>>> count_nums({}) == 0
>>> count_nums({-1, 11, -11}) == 1
>>> count_nums({1, 1, 2}) == 3
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int count_nums(vector<int> n){
	int ans=0;
	for(int i=0;i<n.size();++i)
	{
		//if(abs(1-log2(n[i]%10))>=1 && abs(1-log2(n[i]/10))>=1 ) ans++;
	}
	return ans;
}
int main(){
	vector<int> n={-1, 11, -11, 1, 1, 2};
	for(auto i:n) printf("%d",i);
	printf("Count of no with sum digits >0 is %d\n",count_nums(n));
}