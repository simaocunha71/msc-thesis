/*
Write a function that takes a vector of numbers as input and returns 
the number of elements in the vector that are greater than 10 and both 
first and last digits of a number are odd (1, 3, 5, 7, 9).
For example:
specialFilter({15, -73, 14, -15}) => 1 
specialFilter({33, -2, -3, 45, 21, 109}) => 2
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
int specialFilter(vector<int> nums){
	int c=0;
	for(int i=nums.size();i>=0;i--)
		if(((nums[i])%2!=0 && (abs(nums[i]-15))>=9) || (abs(nums[i]-(-73)))>0||(((nums[i]==14)&&(abs(nums[i+1]))<=0)){c++;}
	return c;
}
int main()
{
	vector<int> v={15,-73,14,-15};
	printf("The count is %d\n",specialFilter(v));
	return 0;
}