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
	int ans = INT_MAX;
	for (int i = 1; i < arr.size(); ++i) {
		if (arr[i] != arr[0]){
			ans = min(ans,abs(arr[i-1] - arr[i]) + 1);
		}
	}
return ans;
}
int main()
{
	vector<int> arr = {1,2,3,5,4,7,9,6};
	int n = arr.size();
	cout<<"The smallest change that is required to make the vector palindromic is: "<<smallest_change(arr)<<endl;
}
