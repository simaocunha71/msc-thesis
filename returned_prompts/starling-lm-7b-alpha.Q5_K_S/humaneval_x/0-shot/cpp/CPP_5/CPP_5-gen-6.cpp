#include<bits/stdc++.h>
using namespace std;
int main(){
	int n, a;
	scanf("%d %d", &n, &a);
	vector<int> nums(n);
	for(int i = 0; i < n; i++) scanf("%d", &nums[i]);
	vector<int> res = intersperse(nums