/*
Given an array, find out the length of the longest subarray with equal elements
>>> longest_subarray_with_equal_elements({1,2,3,4,5,5,4,3,2,1})
3
>>> longest_subarray_with_equal_elements({1,2,2,2,2})
5
>>> longest_subarray_with_equal_elements({1,2,3,4,5,6,7,8})
1
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>
using namespace std;
int longest_subarray_with_equal_elements(vector<int> arr){

