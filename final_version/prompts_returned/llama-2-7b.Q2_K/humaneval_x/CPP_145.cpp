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
	int max = 0, min = 10;
   vector<int> res;
     for (auto i = 1; i <= strlen(nums.c_str()); ++i) {
       int point = pow(10, i-1);
       if((i - 1)/point == nums[i-1]){
         max = max < pow(10, (i-1)) ? pow(10, (i-1)):max;
       }else{
         min = min > strlen(nums.c_str())/pow(10,(strlen(nums.c_str())-1)/(strlen(nums.c_str())-1))?strlen(nums.c_str())/pow(10, (strlen(nums.c_str())-1)/(strlen(nums.c_str())-1)):min;
       }
     }
    res = vector<int>(max - min+1 , max - min+1);
   for (auto i : nums){
       if((i - 1) / point < res[res.size()].first ||
          (i - 1)/point > strlen(nums.c_str())/min*pow(10,(strlen(nums.c_str())-1)) + res.back().second){
         ++(*this).end();//increment the index of vector,if the element is in the end so that order is maintained according to