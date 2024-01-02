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
	int len = nums.size();
	if (len < 1)
	    return -1;
	long long i,j,sum,minSum = INT_MAX;
	for (i=0;i<len;i++){
	    sum = min(nums[i],INT_MIN);//getting the minimum element for every subarray
	    if (sum < 1) break;
	    j = i+1;
	    //sum = sum + nums[j];
        while (j<len && nums[j] >=0){
            sum += nums[j];
            j++;
        }
        minSum = min(minSum,sum);
    }
    return minSum;
}
int main(){
	vector<long long> v({2,-1,-3});
	printf("%d\n",minSubArraySum(v));
}