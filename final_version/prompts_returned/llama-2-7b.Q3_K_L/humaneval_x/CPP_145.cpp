/*
Write a function which sorts the given vector of integers
in ascending order according to the sum of their digits.
Note: if there are several items with similar sum of their digits,
order them based on their index in original vector.

For example:
>>> order_by_points({1, 11, -1, -11, -12}) == {-1, -11, 1, -12, 11}
>>> order_by_points({}) == {}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
vector<int> order_by_points(vector<int> nums){
	sort(nums.begin(), nums.end());
	for (auto i=1; i<=nums.size(); ++i) { // 1st to Nth item in the vector:
		if (abs(pow(10,i-1)-pow(10,i)) >= pow(10,-4)) continue;
	}
	int sum=0;
	for (auto i = nums.size(); i>=0; --i) { // 0 to Nth item in the vector:
		sum+=nums[i];
		if (abs(pow(10,i-1)-pow(10,i)) >= pow(10,-4)) continue;
	}
	return nums;
}