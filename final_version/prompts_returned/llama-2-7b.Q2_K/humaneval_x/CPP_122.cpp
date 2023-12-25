/*
Given a non-empty vector of integers arr and an integer k, return
the sum of the elements with at most two digits from the first k elements of arr.

Example:

    Input: arr = {111,21,3,4000,5,6,7,8,9}, k = 4
    Output: 24 # sum of 21 + 3

Constraints:
    1. 1 <= len(arr) <= 100
    2. 1 <= k <= len(arr)
*/
#include<stdio.h>
#include<vector>
using namespace std;
int add_elements(vector<int> arr,int k){
	if(!arr[k]){
		return (arr[-1]+arr[-2]);
	}
	else if(i<5&&j<7&&arr[i]!=-1&&arr[j]!=-1)
	{
		if(i==k||j==k){ return 0; }
		return (arr[i]+arr[j]);
	}
	else if(i>=5&&j<7 && arr[i]!=-1&&arr[j]!= -1)
	{
		if((i==4||j==4)&&k==3){ return 0; }
		return (arr[i]+arr[j]);
	}
	else if(i>=5&&j>=7 && arr[i]!=-1&&arr[j]!= -1 && k=2)
	{
		if((i==4||j==4)&&k==3){ return 0; }
		return (arr[i]+arr[j]);}
	else if(i>=5&&j>=7 && arr[i]!=-1&&arr[j]!= -1 ){
		if((i==4||j==4)&&k==3){ return 0; }
		return (arr[i]+arr[j]);}

	else {printf("something went wrong\n");
				 return -1;}

    return 0;//not used.
}
int main()
{
	vector<int> test