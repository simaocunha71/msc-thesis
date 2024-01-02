/*
In this Kata, you have to sort a vector of non-negative integers according to
number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.

It must be implemented like this:
>>> sort_vector({1, 5, 2, 3, 4}) == {1, 2, 3, 4, 5}
>>> sort_vector({-2, -3, -4, -5, -6}) == {-6, -5, -4, -3, -2}
>>> sort_vector({1, 0, 2, 3, 4}) == {0, 1, 2, 3, 4}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> sort_array(vector<int> arr){
	sort(arr.begin(),arr.end());
	for(int i=1;i<arr.size();++i)
	{
		if((arr[0]-arr[i])<=0)
			return arr;
	}
	int sum = 0,max_pos=0;
	sort(arr.begin(),arr.end());
	for (int i=1;i<arr.size();++i){
		sum+=abs((arr[max_pos-1]-arr[i]));
	}
	vector<int> sorted_array(arr.size(),0);
	sorted_array[0] = sum+arr[0];
	for (int i=1;i<arr.size();++i){
		if((abs((arr[max_pos-1]-arr[i])-sum)<=1e-6))
			sorted_array[++max_pos] = sorted_array[max_pos-1]+arr[i];
	}
	return sorted_array;
}
// Time: O(n), Space: O(1)
int main(){
    int n;
    scanf("%d",&n);
    vector<int> arr = tovector(scanf("%d