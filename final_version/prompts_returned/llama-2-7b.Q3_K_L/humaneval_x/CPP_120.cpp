/*
Given a vector arr of integers and a positive integer k, return a sorted vector 
of length k with the maximum k numbers in arr.

Example 1:

    Input: arr = {-3, -4, 5}, k = 3
    Output: {-4, -3, 5}

Example 2:

    Input: arr = {4, -4, 4}, k = 2
    Output: {4, 4}

Example 3:

    Input: arr = {-3, 2, 1, 2, -1, -2, 1}, k = 1
    Output: {2}

Note:
    1. The length of the vector will be in the range of {1, 1000}.
    2. The elements in the vector will be in the range of {-1000, 1000}.
    3. 0 <= k <= len(arr)
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
	sort(arr.begin(),arr.end());
	vector<int> temp(k);
	size_t i=0;
	for(int j=0;j<=k-1;j++){
		if(i==k-1)
		{
			temp[j]=arr[j];
		}else
		{
			while(temp[i]<arr[j])
			{
				int t;
				t=arr[i];
				temp[i]=arr[j];
				i++;
			}
		}
	}
	return temp;
}
void main()
{
	vector<int> arr={-3, -4, 5};
	cout<<maximum(arr,3);
}