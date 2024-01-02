/*
Given a non-empty vector of integers, return the sum of all of the odd elements that are in even positions.


Examples
solution({5, 8, 7, 1}) ==> 12
solution({3, 3, 3, 3, 3}) ==> 9
solution({30, 13, 24, 321}) ==>0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int solutions(vector<int> lst){
	int i=0,j=0,sum=0,n=(int)lst.size();
	for(i = 0; i < (int)lst.size(); i++)
	{
		if(lst[i]%2==1 && j<n-2){
			sum+=lst[j+1];
		}
	}
	return sum;
}
int main(){
	vector<int> v={5, 8, 7, 1};
	printf("%d",solutions(v));
	return 0;
}
