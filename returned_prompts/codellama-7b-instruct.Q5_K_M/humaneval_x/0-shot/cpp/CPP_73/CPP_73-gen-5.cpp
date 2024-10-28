/*
Given a vector of integers, find the minimum number of elements that need to be changed
to make the vector palindromic. A palindromic vector is a vector that is read the same
backwards and forwards. In one change, you can change one element to any other element.

For example:
smallest_change({1,2,3,5,4,7,9,6}) == 4
smallest_change({1, 2, 3, 4, 3, 2, 2}) == 1
smallest_change({1, 2, 3, 2, 1}) == 0
*/
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){

int ans = 0;
int n = arr.size();
vector<int> dp(n, 0);
for (int i = 0; i < n; i++) {
	if (arr[i] == arr[n - i - 1]) continue;
	dp[i] = 2;
	ans++;
}
for (int i = 1; i < n; i++) {
	if (arr[i] == arr[n - i - 1]) continue;
	dp[i] = min(dp[i], dp[i - 1] + 1);
}
for (int i = n - 2; i >= 0; i--) {
	if (arr[i] == arr[n - i - 1]) continue;
	dp[i] = min(dp[i], dp[i + 1] + 1);
}
return ans + dp[0];
}
}











































































































