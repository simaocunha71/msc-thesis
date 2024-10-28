
#include <bits/stdc++.h>

using namespace std;

int minSubArraySum(vector<int>& nums) {
    int n = nums.size(),ans = 0x3f3f3f3f3f3f3f3f;
    int cur = 0;
    for(int i = 0;i < n;i++)
    {
        cur += nums[i];
        for(int j = 0;j < i;j++)
           