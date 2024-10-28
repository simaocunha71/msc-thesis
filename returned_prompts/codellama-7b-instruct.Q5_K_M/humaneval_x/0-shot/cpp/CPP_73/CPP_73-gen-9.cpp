/*
Given a vector arr of integers, find the minimum number of elements that
need to be changed to make the vector palindromic. A palindromic vector is a vector that
is read the same backwards and forwards. In one change, you can change one element to any other element.

For example:
smallest_change({1,2,3,5,4,7,9,6}) == 4
smallest_change({1, 2, 3, 4, 3, 2, 2}) == 1
smallest_change({1, 2, 3, 2, 1}) == 0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int n = arr.size();
    vector<int> dp(n, n);
    for (int i = 0; i < n; i++) dp[i] = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] == arr[j]) {
                dp[i] = min(dp[i], 1 + dp[j]);
            }
            else {
                dp[i] = min(dp[i], 1 + dp[j]);
            }
        }
    }
    return dp[n-1];
}
// @lc code=end
