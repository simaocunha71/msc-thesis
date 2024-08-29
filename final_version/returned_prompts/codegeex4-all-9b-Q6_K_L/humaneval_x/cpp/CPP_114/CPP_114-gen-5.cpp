/*
The above code defines a function minSubArraySum that takes a vector of integers as input and returns the minimum sum of any non-empty sub-vector of nums. 
The function uses a dynamic programming approach to solve the problem. 
It initializes an array dp of size n+1, where n is the size of nums. 
The dp[i] represents the minimum sum of a sub-vector ending at index i. 
The function then iterates over the nums array and updates dp[i] based on the minimum sum of the sub-vectors ending at index i-1 and the current element nums[i]. 
Finally, the function returns the minimum value in dp as the result. 
This approach has a time complexity of O(n) and a space complexity of O(n), where n is the size of nums. 
*/

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
long long minSubArraySum(vector<long long> nums){
    int n = nums.size();
    vector<long long> dp(n+1, 0);
    for(int i=1; i<=n; i++){
        dp[i] = min(dp[i-1], 0) + nums[i-1];
    }
    return *min_element(dp.begin(), dp.end());
}