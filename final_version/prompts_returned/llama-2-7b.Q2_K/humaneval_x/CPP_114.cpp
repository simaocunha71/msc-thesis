/*
Given a vector of integers nums, find the minimum sum of any non-empty sub-vector
of nums.
Example
minSubArraySum({2, 3, 4, 1, 2, 4}) == 1
minSubArraySum({-1, -2, -3}) == -6
*/
#include<stdio.h>
#include<vector>
using namespace std;
long long minSubArraySum(vector<long long> nums){
	int sub=0;
	for(int i = 0 ;i < nums.size(); i++){sub+=nums[i];}

	for(int j=1;j<nums.size();j++){
		if(sub>=0)break;
		sub-=(nums[j-1]**2);
	}
	return sub;
}

